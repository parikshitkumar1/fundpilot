import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests
import json
import tkinter as tk
from tkinter import simpledialog

def load_model():
    """Initialize connection to Ollama API with Llama2"""
    try:
        # Test connection to Ollama
        response = requests.post('http://localhost:11434/api/generate', 
            json={
                "model": "llama2",  # Using llama2 instead of mixtral
                "prompt": "test",
                "stream": False
            })
        if response.status_code == 200:
            print("✓ Successfully connected to Ollama API")
            return True
        else:
            raise ConnectionError("Could not connect to Ollama API")
    except Exception as e:
        print(f"❌ Error connecting to Ollama: {str(e)}")
        print("Please make sure you have:")
        print("1. Installed Ollama (https://ollama.ai)")
        print("2. Started the Ollama service")
        print("3. Pulled the llama2 model using: ollama pull llama2")
        raise

def generate_answer(prompt, context_data, max_length=150, dropdown_options=None):
    clean_prompt = prompt.lower().strip()
    from difflib import get_close_matches

    # Gender breakdown logic
    if "gender breakdown" in clean_prompt:
        founders = context_data.get('Team Information.Founders', '')
        names = [n.strip().lower() for n in founders.split(',')]
        male_names = {"john", "sam"}
        female_names = {"jane"}
        male_count = sum(1 for n in names if n.split()[0] in male_names)
        female_count = sum(1 for n in names if n.split()[0] in female_names)
        if male_count and female_count:
            return "Mixed team"
        elif male_count:
            return "All male"
        elif female_count:
            return "All female"
        else:
            return ""

    # Student/recent graduate logic
    if "student" in clean_prompt or "recent graduate" in clean_prompt:
        bios = context_data.get('Team Information.Key Team Members', '') + " " + context_data.get('Team Information.Founders', '')
        keywords = ["student", "graduate", "university", "college"]
        if any(k in bios.lower() for k in keywords):
            return "Yes"
        else:
            return "No"

    # Location logic
    if ("where" in clean_prompt and "located" in clean_prompt) or ("location" in clean_prompt):
        return context_data.get('Business Information.Location', '')

    # Pitchdeck logic
    if "pitchdeck" in clean_prompt:
        return ""  # Skip if no info

    # Unique about startup (4-5 sentences)
    if ("unique" in clean_prompt or "what is unique" in clean_prompt) and ("sentence" in clean_prompt or "sentences" in clean_prompt):
        system_context = (
            "You are an AI assistant. Write a compelling, specific, and concise 4-5 sentence answer about what is unique about this startup, using the following information:\n"
            f"Mission: {context_data.get('Business Information.Mission Statement', '')}\n"
            f"Innovation: {context_data.get('Product or Service Description.Innovation', '')}\n"
            f"Differentiation: {context_data.get('Product or Service Description.Differentiation', '')}\n"
            f"Problem Solved: {context_data.get('Product or Service Description.Problem Solved', '')}\n"
            f"Target Market: {context_data.get('Market Opportunity.Target Market', '')}\n"
        )
        formatted_prompt = f"{system_context}\nQuestion: {prompt}\nAnswer (4-5 sentences):"
        try:
            response = requests.post('http://localhost:11434/api/generate',
                json={
                    "model": "llama2",
                    "prompt": formatted_prompt,
                    "stream": False,
                    "temperature": 0.2,
                    "max_tokens": max_length,
                    "top_p": 0.9
                })
            if response.status_code == 200:
                answer = response.json()['response'].strip()
                answer = " ".join(answer.split())
                return answer[:max_length]
            else:
                raise Exception(f"Error from Ollama API: {response.text}")
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Error generating response"

    # Check for simple direct questions that don't need LLM processing
    if "name of your company" in clean_prompt:
        return context_data.get('Business Information.Business Name', '')
    elif "website" in clean_prompt:
        return context_data.get('Business Information.Website', '')
    elif "location" in clean_prompt or "where" in clean_prompt and "located" in clean_prompt:
        location = context_data.get('Business Information.Location', '')
        # Remove placeholder text if present
        location = location.replace('[City]', '').replace('[State]', '').strip()
        # Remove multiple spaces and commas
        location = ' '.join(part.strip() for part in location.split(','))
        return location
    elif "founding team" in clean_prompt or ("who" in clean_prompt and "team" in clean_prompt):
        founders = context_data.get('Team Information.Founders', '')
        # Clean up the founders string to just be comma-separated names
        return ', '.join(name.strip() for name in founders.split(','))
    elif "funding" in clean_prompt and "raise" in clean_prompt:
        funding = context_data.get('Financial Projections.Funding Allocation', '')
        # Extract just the number if it's a string with currency symbols
        if isinstance(funding, str):
            funding = ''.join(filter(str.isdigit, funding))
        return funding  # Return without $ as the form probably has its own format
    elif "launch" in clean_prompt or "when did you start" in clean_prompt:
        year = context_data.get('Business Information.Year Established')
        if year:
            try:
                year = int(year)
                current_year = 2025
                if year < current_year - 1:
                    return "More than 1 year ago"
                elif year == current_year:
                    return "Less than 6 months ago"
                else:
                    return "6-12 months ago"
            except:
                return "More than 1 year ago"
        return "More than 1 year ago"
    elif "elevator pitch" in clean_prompt or "describe your business" in clean_prompt:
        mission = context_data.get('Business Information.Mission Statement', '')
        problem = context_data.get('Product or Service Description.Problem Solved', '')
        combined = f"{mission} {problem}"
        max_chars = 140
        return combined[:max_chars].strip()
    elif "industry" in clean_prompt:
        industry_csv = context_data.get('Market Opportunity.Target Market', '')
        # If dropdown options are provided, fuzzy match
        if dropdown_options:
            labels = [opt.strip() for opt in dropdown_options if opt.strip().lower() != 'choose']
            close = get_close_matches(industry_csv, labels, n=1, cutoff=0.5)
            if close:
                return close[0]
        # Otherwise, return the cleaned CSV value
        return industry_csv

    # For more complex questions, use the LLM with strict formatting
    system_context = f"""You are writing responses for a startup funding application form. Follow these rules:
1. Never use conversational language
2. Never add explanatory text
3. Match the exact format requested in the question
4. Keep responses under any specified character limit
5. For team/founder questions, only list names unless bios are specifically requested
6. For funding questions, always include the $ symbol
7. For timing questions, match the exact options available (e.g. "More than 1 year ago", "6-12 months ago", etc.)

Available company information:
COMPANY: {context_data.get('Business Information.Business Name')}
MISSION: {context_data.get('Business Information.Mission Statement')}
PROBLEM: {context_data.get('Product or Service Description.Problem Solved')}
MARKET: {context_data.get('Market Opportunity.Target Market')}
TEAM: {context_data.get('Team Information.Founders')}
FUNDING: ${context_data.get('Financial Projections.Funding Allocation')}"""

    formatted_prompt = f"{system_context}\n\nQuestion: {prompt}\n\nProvide exact answer:"

    try:
        response = requests.post('http://localhost:11434/api/generate',
            json={
                "model": "llama2",
                "prompt": formatted_prompt,
                "stream": False,
                "temperature": 0.2,  # Even lower temperature for more consistent outputs
                "max_tokens": max_length,
                "top_p": 0.9
            })
        
        if response.status_code == 200:
            answer = response.json()['response'].strip()
            
            # Clean up any remaining conversational elements
            answer = answer.replace("Here is", "").replace("Here are", "")
            answer = answer.replace("Sure,", "").replace("I'd be happy to", "")
            answer = answer.replace("To answer your question,", "")
            
            # Clean up any line breaks or multiple spaces
            answer = " ".join(answer.split())
            
            # If it's a character-limited question, ensure we respect the limit
            if "characters" in clean_prompt:
                max_chars = 140  # default
                if "140" in clean_prompt:
                    max_chars = 140
                answer = answer[:max_chars]
            
            return answer.strip()
        else:
            raise Exception(f"Error from Ollama API: {response.text}")
            
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Error generating response"

def read_applicant_data(csv_file="funding_application.csv"):
    try:
        df = pd.read_csv(csv_file)
        data_dict = df.iloc[0].to_dict()
        
        # Validate required fields
        required_fields = [
            'Business Information.Business Name',
            'Business Information.Mission Statement',
            'Product or Service Description.Problem Solved',
            'Market Opportunity.Target Market',
            'Team Information.Founders'
        ]
        
        missing_fields = [field for field in required_fields if not data_dict.get(field)]
        if missing_fields:
            print(f"Warning: Missing required fields: {', '.join(missing_fields)}")
            
        # Clean and standardize the data
        for key, value in data_dict.items():
            if isinstance(value, str):
                # Remove extra whitespace and standardize formatting
                data_dict[key] = ' '.join(value.split())
            elif pd.isna(value):
                data_dict[key] = ''
                
        return data_dict
    except FileNotFoundError:
        print(f"Error: Could not find CSV file: {csv_file}")
        return {}
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        return {}

def fill_web_form(form_url, data_dict, client):
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.common.exceptions import ElementClickInterceptedException

    print(f"Opening form: {form_url}")
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    actions = ActionChains(driver)
    driver.get(form_url)
    time.sleep(5)  # Wait for form to load

    # Updated selectors for Google Forms
    questions = driver.find_elements(By.CSS_SELECTOR, ".Qr7Oae")
    print(f"Found {len(questions)} questions in the form")

    for question in questions:
        try:
            # Get full question text including any helper text
            question_text = ""
            try:
                heading = question.find_element(By.CSS_SELECTOR, ".M7eMe").text.strip()
                question_text = heading
                # Try to get additional helper text if present
                try:
                    helper_text = question.find_element(By.CSS_SELECTOR, ".z12JJ").text.strip()
                    if helper_text:
                        question_text += " " + helper_text
                except:
                    pass
            except:
                continue

            if not question_text or "start" in question_text.lower() or "easy peasy" in question_text.lower():
                continue

            print(f"Processing question: {question_text[:100]}...")
            
            # Scroll question into view
            driver.execute_script("arguments[0].scrollIntoView(true);", question)
            time.sleep(0.5)  # Wait for scroll to complete
            
            # Determine input type with more robust detection
            input_type = None
            try:
                if question.find_elements(By.CSS_SELECTOR, "[role='radio']"):
                    input_type = "radio"
                elif question.find_elements(By.CSS_SELECTOR, "[role='listbox']"):
                    input_type = "dropdown"
                elif question.find_elements(By.CSS_SELECTOR, "div[role='checkbox']"):
                    input_type = "checkbox"
                elif question.find_elements(By.CSS_SELECTOR, ".uHMk6b.fsHoPb"):
                    input_type = "yesno"
                elif question.find_elements(By.CSS_SELECTOR, "textarea"):
                    input_type = "textarea"
                elif question.find_elements(By.CSS_SELECTOR, "input[type='text']"):
                    input_type = "text"
                elif question.find_elements(By.CSS_SELECTOR, "input[type='email']"):
                    input_type = "email"
            except:
                pass

            if not input_type:
                # Try alternate selectors
                try:
                    if question.find_elements(By.CSS_SELECTOR, ".AB7Lab"):  # Radio buttons
                        input_type = "radio"
                    elif question.find_elements(By.CSS_SELECTOR, ".MocG8c"):  # Dropdown
                        input_type = "dropdown"
                    elif question.find_elements(By.CSS_SELECTOR, ".KHxj8b"):  # Long text
                        input_type = "textarea"
                    elif question.find_elements(By.CSS_SELECTOR, ".whsOnd"):  # Short text
                        input_type = "text"
                except:
                    pass

            if not input_type:
                print(f"⚠️ Could not determine input type for: {question_text[:50]}...")
                continue

            # Generate answer based on question content
            clean_question = question_text.lower()
            dropdown_options = None
            if input_type == "dropdown":
                dropdown = question.find_element(By.CSS_SELECTOR, "[role='listbox']")
                dropdown.click()
                time.sleep(0.5)
                dropdown_options = [opt.text for opt in driver.find_elements(By.CSS_SELECTOR, "[role='option']")]
                dropdown.click()  # Close dropdown
            answer = generate_answer(clean_question, data_dict, dropdown_options=dropdown_options)

            if answer:
                success = False
                max_attempts = 3
                attempt = 0
                from difflib import get_close_matches
                def normalize(s):
                    return ''.join(c for c in s.lower() if c.isdigit())
                while not success and attempt < max_attempts:
                    try:
                        if input_type == "radio":
                            options = question.find_elements(By.CSS_SELECTOR, "[role='radio']")
                            answer_norm = normalize(answer)
                            for option in options:
                                try:
                                    label = option.text.strip()
                                    label_norm = normalize(label)
                                    # Match if numbers match or answer is in label
                                    if answer_norm and (answer_norm == label_norm or answer_norm in label_norm or label_norm in answer_norm):
                                        try:
                                            option.click()
                                        except:
                                            try:
                                                actions.move_to_element(option).click().perform()
                                            except:
                                                driver.execute_script("arguments[0].click();", option)
                                        success = True
                                        break
                                except:
                                    continue
                        
                        elif input_type == "dropdown":
                            try:
                                dropdown = question.find_element(By.CSS_SELECTOR, "[role='listbox']")
                                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[role='listbox']")))
                                actions.move_to_element(dropdown).click().perform()
                                time.sleep(0.5)
                                options = driver.find_elements(By.CSS_SELECTOR, "[role='option']")
                                print(f"Dropdown options: {[option.text for option in options]}")
                                print(f"Generated answer: {answer}")
                                answer_norm = normalize(answer)
                                matched = False
                                for option in options:
                                    label = option.text.strip()
                                    label_norm = normalize(label)
                                    if answer_norm and (answer_norm == label_norm or answer_norm in label_norm or label_norm in answer_norm):
                                        wait.until(EC.element_to_be_clickable(option))
                                        actions.move_to_element(option).click().perform()
                                        success = True
                                        matched = True
                                        break
                                if not matched:
                                    # Fuzzy match for industry dropdowns
                                    if "industry" in clean_question:
                                        labels = [option.text.strip() for option in options]
                                        close = get_close_matches(answer, labels, n=1, cutoff=0.6)
                                        if close:
                                            for option in options:
                                                if option.text.strip() == close[0]:
                                                    actions.move_to_element(option).click().perform()
                                                    success = True
                                                    matched = True
                                                    break
                                    # Fallback: select first option if still no match
                                    if not matched and options:
                                        actions.move_to_element(options[0]).click().perform()
                                        print(f"⚠️ Fallback: selected first dropdown option for: {question_text[:50]}...")
                                        success = True
                                actions.move_by_offset(0, 100).click().perform()  # Click outside to close
                                if not success:
                                    print(f"⚠️ No matching dropdown option for: {answer}")
                            except ElementClickInterceptedException:
                                driver.execute_script("arguments[0].scrollIntoView(true);", dropdown)
                                time.sleep(0.5)
                                continue
                        elif input_type == "checkbox":
                            if answer.lower() in ["yes", "true", "checked", "tick"]:
                                checkbox = question.find_element(By.CSS_SELECTOR, "div[role='checkbox']")
                                if "aria-checked=\"false\"" in checkbox.get_attribute("outerHTML"):
                                    checkbox.click()
                                success = True
                        elif input_type == "yesno":
                            buttons = question.find_elements(By.CSS_SELECTOR, ".uHMk6b.fsHoPb")
                            for btn in buttons:
                                if answer.lower() in btn.text.lower():
                                    btn.click()
                                    success = True
                                    break
                        else:
                            # Handle text inputs
                            input_field = None
                            if input_type == "textarea":
                                input_field = question.find_element(By.CSS_SELECTOR, "textarea")
                            elif input_type == "email":
                                input_field = question.find_element(By.CSS_SELECTOR, "input[type='email']")
                            else:
                                input_field = question.find_element(By.CSS_SELECTOR, "input[type='text']")
                            if input_field:
                                wait.until(EC.element_to_be_clickable(input_field))
                                input_field.clear()
                                input_field.send_keys(answer)
                                success = True
                        if success:
                            print(f"✓ Filled: {question_text[:50]}...")
                            break
                    except Exception as e:
                        print(f"Attempt {attempt + 1} failed: {str(e)}")
                        attempt += 1
                        time.sleep(0.5)
                if not success:
                    print(f"⚠️ Could not fill after {max_attempts} attempts: {question_text[:50]}...")
            
            else:
                print(f"⚠️ No answer generated for: {question_text[:50]}...")

            time.sleep(0.5)
                
        except Exception as e:
            print(f"❌ Error processing question: {str(e)}")

    print("\n✅ Form filling completed!")
    print("The browser will stay open for 5 minutes so you can review and submit.")
    print("Please review all answers carefully before submitting.")
    time.sleep(300)
    driver.quit()

def main():
    try:
        # Use a popup dialog to get the form URL
        root = tk.Tk()
        root.withdraw()
        form_url = simpledialog.askstring("Form URL", "Enter the online form URL:")
        root.destroy()
        if not form_url:
            print("Error: Form URL cannot be empty")
            return
        print("\n1. Loading application data...")
        data = read_applicant_data()
        if not data:
            print("Error: Could not load application data. Please check your CSV file.")
            return
        print("\n2. Initializing AI model...")
        client = load_model()
        if not client:
            return
        print("\n3. Starting form fill process...")
        fill_web_form(form_url, data, client)
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {str(e)}")
        print("If the error persists, please check your internet connection and API key.")

if __name__ == "__main__":
    main()
