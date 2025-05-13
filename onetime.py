import streamlit as st
import pandas as pd
import os
import PyPDF2
from docx import Document

# Function to format responses into a structured format
def format_responses(responses):
    formatted_data = {
        "Business Information": {
            "Business Name": responses["business_name"],
            "Legal Structure": responses["legal_structure"],
            "Location": responses["location"],
            "Website": responses["website"],
            "Year Established": responses["established_year"],
            "Mission Statement": responses["mission_statement"],
            "Core Products/Services": responses["core_products_services"]
        },
        "Product or Service Description": {
            "Problem Solved": responses["problem_solved"],
            "Innovation": responses["innovation"],
            "Differentiation": responses["differentiation"],
            "Development Stage": responses["development_stage"],
            "IP Rights": responses["ip_rights"]
        },
        "Market Opportunity": {
            "Target Market": responses["target_market"],
            "Market Size": responses["market_size"],
            "Key Trends": responses["key_trends"],
            "Market Share Goal": responses["market_share_goal"],
            "Competitors": responses["competitors"],
            "Demand": responses["demand"]
        },
        "Financial Projections": {
            "Revenue Model": responses["revenue_model"],
            "Current Revenue": responses["current_revenue"],
            "Projected Revenue": responses["projected_revenue"],
            "Break-even Point": responses["break_even_point"],
            "Operating Costs": responses["operating_costs"],
            "Funding Allocation": responses["funding_allocation"]
        },
        "Team Information": {
            "Founders": responses["founders"],
            "Key Team Members": responses["key_team_members"],
            "Skills Missing": responses["skills_missing"],
            "Advisors": responses["advisors"]
        },
        "Impact and Social Responsibility": {
            "Social/Environmental Impact": responses["social_impact"],
            "Sustainability Efforts": responses["sustainability_efforts"],
            "Community Benefits": responses["community_benefits"]
        },
        "Sales and Marketing Strategy": {
            "Go-to-market Strategy": responses["go_to_market_strategy"],
            "Customer Acquisition Strategy": responses["customer_acquisition_strategy"],
            "Sales Channels": responses["sales_channels"],
            "Marketing Campaign Success": responses["marketing_campaign_success"]
        },
        "Legal and Regulatory": {
            "Compliance": responses["compliance"],
            "Legal Risks": responses["legal_risks"],
            "Patents/Trademarks": responses["patents_trademarks"]
        },
        "Exit Strategy": {
            "Exit Strategy": responses["exit_strategy"],
            "Ideal Acquirer": responses["ideal_acquirer"],
            "Exit Timeline": responses["exit_timeline"]
        },
        "Growth and Scaling": {
            "Scaling Plans": responses["scaling_plans"],
            "Growth Projections": responses["growth_projections"]
        },
    }
    return formatted_data

# Function to flatten nested dictionary for CSV saving
def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Function to parse resume content
def parse_resume(file_path):
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
            return text
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    else:
        return "Unsupported file format"

# Main Streamlit application
def app():
    st.title("One time setup")

    # Create a dictionary to store responses
    responses = {}

    # Collect all responses
    st.header("Business Information")
    responses["business_name"] = st.text_input("What is the name of your business?")
    responses["legal_structure"] = st.text_input("What is the legal structure of your business?")
    responses["location"] = st.text_input("What is the location of your business?")
    responses["website"] = st.text_input("What is your company’s website?")
    responses["established_year"] = st.number_input("When was your business established?", min_value=1900, max_value=2025)
    responses["mission_statement"] = st.text_area("What is your business’s mission statement?")
    responses["core_products_services"] = st.text_area("What are your company’s core products or services?")

    st.header("Product or Service Description")
    responses["problem_solved"] = st.text_area("What problem does your product/service solve?")
    responses["innovation"] = st.text_area("What is the innovation behind your product/service?")
    responses["differentiation"] = st.text_area("How does your product or service differentiate from competitors?")
    responses["development_stage"] = st.text_input("What is the current stage of development for your product/service?")
    responses["ip_rights"] = st.text_area("What intellectual property (IP) rights, patents, or trademarks does your company hold?")

    st.header("Market Opportunity")
    responses["target_market"] = st.text_area("Who is your target market?")
    responses["market_size"] = st.text_input("What is the size of the market you’re targeting?")
    responses["key_trends"] = st.text_area("What are the key trends influencing your market?")
    responses["market_share_goal"] = st.text_input("What’s the estimated market share you plan to capture?")
    responses["competitors"] = st.text_area("Who are your competitors, and how do you compare to them?")
    responses["demand"] = st.text_area("What’s the demand for your product/service in the market?")

    st.header("Financial Projections")
    responses["revenue_model"] = st.text_input("What is your revenue model?")
    responses["current_revenue"] = st.text_input("How much revenue do you currently generate?")
    responses["projected_revenue"] = st.text_input("What is your projected revenue for the next 1–3 years?")
    responses["break_even_point"] = st.text_input("What is your break-even point?")
    responses["operating_costs"] = st.text_input("What are your projected operating costs?")
    responses["funding_allocation"] = st.text_area("How will you allocate the funding?")

    st.header("Team Information")
    responses["founders"] = st.text_area("Who are the key members of your team and what are their roles?")
    responses["key_team_members"] = st.text_area("What relevant experience or expertise do the founders/team members bring?")
    responses["skills_missing"] = st.text_area("What skills or expertise are you currently missing from your team?")
    responses["advisors"] = st.text_area("Do you have any advisors or mentors? If so, who are they and how do they contribute?")

    st.header("Impact and Social Responsibility")
    responses["social_impact"] = st.text_area("What social or environmental impact does your business have?")
    responses["sustainability_efforts"] = st.text_area("How does your business contribute to sustainability?")
    responses["community_benefits"] = st.text_area("How does your business create jobs, improve education, or provide other community benefits?")

    st.header("Sales and Marketing Strategy")
    responses["go_to_market_strategy"] = st.text_area("What is your go-to-market strategy?")
    responses["customer_acquisition_strategy"] = st.text_area("How do you plan to acquire customers?")
    responses["sales_channels"] = st.text_area("What sales channels are you using?")
    responses["marketing_campaign_success"] = st.text_area("What marketing campaigns have been successful for you so far?")

    st.header("Legal and Regulatory")
    responses["compliance"] = st.text_area("Is your business fully compliant with local, state, and federal regulations?")
    responses["legal_risks"] = st.text_area("Are there any legal risks or challenges in your business?")
    responses["patents_trademarks"] = st.text_area("Do you hold any patents, trademarks, or other intellectual property protections?")

    st.header("Exit Strategy")
    responses["exit_strategy"] = st.text_input("What is your long-term vision for the business?")
    responses["ideal_acquirer"] = st.text_input("Who would be your ideal acquirer or partner?")
    responses["exit_timeline"] = st.text_input("What’s your timeline for reaching an exit?")

    st.header("Growth and Scaling")
    responses["scaling_plans"] = st.text_area("How do you plan to scale your business in the next 1–3 years?")
    responses["growth_projections"] = st.text_area("What are your growth projections for the next 1–5 years?")

    st.header("Resume Upload")
    resume = st.file_uploader("Attach your resume (optional)", type=["pdf", "docx"])

    # After form completion, show the summary and allow download
    if st.button("Submit"):
        formatted_data = format_responses(responses)

        # Flatten the data for CSV saving
        flattened_data = flatten_dict(formatted_data)
        df = pd.DataFrame([flattened_data])
        df.to_csv("funding_application.csv", index=False)

        if resume is not None:
            resume_path = os.path.join("resumes", resume.name)
            with open(resume_path, "wb") as f:
                f.write(resume.getbuffer())
            st.success("Resume uploaded successfully!")

            # Parse the resume
            parsed_text = parse_resume(resume_path)
            st.text_area("Parsed Resume Content", parsed_text)

if __name__ == "__main__":
    app()
