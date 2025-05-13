# FundPilot - Web Form Filling Automation with AI Model Integration

FundPilot automates the process of filling out web forms using AI models and web automation tools. The AI generates context-aware answers for the form fields, and Selenium is used to fill out the form programmatically. The process is designed to be run offline for privacy and efficiency.

---

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [AI Models](#ai-models)
- [Offline Usage](#offline-usage)
- [Prerequisites](#prerequisites)
- [License](#license)
- [GitHub Repository](#github-repository)

---

## Overview

FundPilot automates web form filling by using AI to generate answers based on user-uploaded resumes and then automatically filling out the form using Selenium. This allows for easy and fast form completion without manual data entry. The tool is designed for offline usage to ensure privacy and data security.

---

## Technologies Used

- **Selenium WebDriver**: Used to automate browser interactions, such as filling out form fields.
- **ChromeDriver**: Required to control the Chrome browser with Selenium.
- **Tkinter**: Used to create a simple GUI for users to input the URL of the form to be filled.
- **AI Models**:
  - **LLaMA 2 7B**: The main model used for generating contextually relevant answers.
- **Streamlit**: Used for running the initial part of the process to generate CSV data.
- **Python**: The programming language for AI model integration, form automation, and CSV handling.

---

## Installation

### Prerequisites

1. **Python 3.x**: Make sure you have Python 3.x installed.
2. **Chrome**: Chrome browser should be installed.
3. **ChromeDriver**: Download and install ChromeDriver compatible with your version of Chrome.
4. **Ollama with LLaMA 2 7B**: Ensure that Ollama is installed and the LLaMA 2 7B model is available for use.

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/parikshitkumar1/fundpilot.git
   cd fundpilot

2. install requirements:
   ```bash
   pip install -r requirements.txt

3. run one-time setup:
   ```bash
   streamlit run onetime.py

4. run co-pilot:
   ```bash
   python fundme.py


# Funding Sources for Early-Stage Startups

## Accelerators & Incubators

* **Y Combinator** (Accelerator) – Invests **\$500K** via a standard deal; open to startups worldwide.  Applications are accepted in multiple annual batches (e.g. Winter ’25 apps due Nov 12, 2024).  Website: [ycombinator.com](https://www.ycombinator.com)
* **Techstars** (Accelerator) – Provides **\$20K** equity investment (plus access to \~\$100K in perks) and an optional **\$100K** convertible note in exchange for \~6%–9% equity.  Runs \~50+ industry-specific programs globally each year; deadlines vary by program (cohorts throughout the year).  Website: [techstars.com](https://www.techstars.com)
* **500 Global Flagship Accelerator** (Accelerator) – Offers **\$150K** in seed investment (about 6% equity).  Based in Silicon Valley but open to startups worldwide.  Next applications (Batch 36) close **Oct 11, 2024**.  Website: [500.co](https://500.co)
* **Entrepreneur First** (Incubator/Accelerator) – Helps founders form teams and ideas, then invests up to **\$125K** (matched by partner for up to **\$250K** total).  Offices in London, Paris, Berlin, SF, Singapore, Bangalore, etc. (global).  Applications are on a rolling basis (multiple cohorts per year).  Website: [joinef.com](https://www.joinef.com)
* **Startupbootcamp** (Accelerator) – Industry-focused programs (e.g. FinTech, DeepTech) in Europe, Asia and Latin America.  Takes \~8% equity in exchange for **€15K** cash stipend.  Application deadlines vary by track (often yearly cycles, e.g. \~Jan for spring cohorts).  Website: [startupbootcamp.org](https://www.startupbootcamp.org)
* **Plug and Play Tech Center** (Accelerator/VC) – Operates 100+ corporate innovation programs worldwide.  Invests through Plug and Play Ventures (seed focus), with typical checks around **\$100K–\$150K**.  Global (30+ offices in US, Europe, APAC).  Application deadlines vary by program; startups can join many cohort intakes year-round.  Website: [plugandplaytechcenter.com](https://www.plugandplaytechcenter.com)
* **Antler** (Accelerator/Incubator) – “Day Zero” investor that teams up with founders pre-company.  Provides **\$100K–\$150K** funding for \~10–12% equity.  Programs run in 25+ cities across 6 continents (e.g. NY, London, Berlin, Singapore, Nairobi, Jakarta).  Applications are open year-round by location.  Website: [antler.co](https://www.antler.co)
* **MassChallenge** (Accelerator) – Global, zero-equity accelerator (no fees or equity).  Runs regional programs in USA, Europe, Latin America, Asia.  Selected startups compete for equity-free cash prizes (past cohorts awarded up to **\$100K** per winner, totaling \~\$1M across winners).  Applications are open annually (multiple deadlines per region).  Website: [masschallenge.org](https://masschallenge.org)

## Angel Networks & Platforms

* **AngelList** (Angel Syndicate Platform) – Startup fundraising and angel network platform (global).  Allows founders to raise seed rounds via accredited angels and online syndicates.  Typical early-stage checks on AngelList are around **\$100K** (median), though amounts vary.  Applications/meetings are rolling via the platform.  Website: [angellist.com](https://www.angellist.com)
* **Angel Investment Network** (Angel Network) – Online platform connecting startups with 366K+ active angel investors worldwide.  Startups post pitches to attract investment ranging from **\$1K** up to **\$1M+** from network members.  Region: Global (offices in 80+ countries).  Operations are ongoing (rolling submissions).  Website: [angelinvestmentnetwork.com](https://www.angelinvestmentnetwork.com)

## Grants & Government Programs

* **EIC Accelerator** (EU Grant/Equity Program) – Part of Horizon Europe for deep-tech SMEs.  Offers grants (lump sums up to **€2.5M** for R\&D) plus equity investments (typically **€0.5–10M**).  Open to EU/associated startups (and global markets).  Deadlines for full proposals: **Mar 12, 2025** and **Oct 1, 2025**.  Website: [eic.ec.europa.eu](https://eic.ec.europa.eu)
* **SBIR/STTR Programs** (US Government Grants) – Federally funded R\&D grants for US small businesses.  Phase I awards are typically up to **\$150K** (R\&D feasibility), Phase II up to \~\$1M+ (development).  Multiple agencies (NIH, DoD, NSF, NASA, etc.) run solicitations with staggered deadlines (e.g. NASA SBIR Phase I closed Mar 10, 2025; other agencies have periodic windows).  Website: [sbir.gov](https://www.sbir.gov)
* **Global Innovation Fund** (Non-Profit Grant/Equity) – Impact-focused fund for social innovations (education, health, etc.) in developing markets.  Funding ranges by stage: up to **\$230K** (pilot), **\$2.3M** (test), up to **\$15M** (scale).  Region: Global (focus on developing countries).  Applications open during rolling “calls” – last round closed Jan 15, 2025 (next to be announced).  Website: [globalinnovation.fund](https://www.globalinnovation.fund)

**Sources:** Official program websites and reputable startup funding guides.


## 📄 Sample Filled Form (Generated Output)

**Name**: John Doe (CEO)  
\
**City, State, Country**  
Where is your project based?  
City: San Francisco, State: California, Country: United States

**Is there a nonprofit, school, church, or business you are a part of that is hosting this project?**  
Please describe relationship.  
No, there is no nonprofit, school, church, or business that is hosting this project. As the founder and CEO of GreenTech Solutions, I am solely responsible for the development and implementation of our sustainable technology solutions.

**E-mail**:  
[johndoe@greentechsolutions.com](mailto:johndoe@greentechsolutions.com)

**Mailing Address**:  
GreenTech Solutions  
123 Main Street  
Anytown, USA 12345

**Phone**:  
+1 (555) 123-4567

---

### 📝 Project Description

GreenTech Solutions aims to revolutionize the way energy is produced and consumed in urban areas through the development of affordable, clean technology solutions. Our initial product offering will focus on creating a smart solar panel system that can be easily integrated into existing rooftops, providing homeowners and small businesses with a reliable and sustainable source of renewable energy.

The system will include advanced monitoring capabilities, allowing users to track their energy production and consumption in real-time. Additionally, the system will be designed to optimize energy production based on weather conditions and time of day, further reducing the carbon footprint of urban areas.

Our market research indicates a significant demand for clean energy solutions in urban areas, with homeowners and small businesses willing to invest in sustainable technology. Our initial target market will be urban areas in North America, with plans to expand to other regions in the near future. To achieve our mission, we require funding of 50% for product development, 30% for marketing, and 20% for operational expansion.

---

### 🤝 How does this project relate to resource sharing or solidarity economics?

The GreenTech Solutions project is directly related to the principles of resource sharing and solidarity economics. Our mission is to provide sustainable and affordable technology solutions that promote a greener future, which aligns with the values of resource sharing and solidarity economics.

By reducing dependency on fossil fuels and promoting clean energy, we are not only contributing to a more sustainable environment but also fostering a sense of community and cooperation among stakeholders. Our solutions aim to make renewable energy accessible to a broader audience, including homeowners, small businesses, and government buildings in urban areas, which is in line with the principles of resource sharing and solidarity economics. By creating a more equitable and sustainable energy system, we are promoting a culture of collaboration and mutual support that benefits both individuals and society as a whole.

---

### 🌍 Impact on Community and Engagement

GreenTech Solutions' project aims to provide sustainable and affordable technology solutions, ultimately contributing to a greener future for our community. Our target market includes homeowners, small businesses, and government buildings in urban areas, where energy consumption is particularly high. By offering cost-effective alternatives to fossil fuels, we will reduce energy dependency, lower carbon emissions, and improve air quality.

To engage the community in the development and maintenance of our project, we plan to establish a Community Engagement Committee (CEC) composed of local residents, business owners, and government officials. The CEC will provide a platform for stakeholders to share their ideas, feedback, and concerns regarding the project. Additionally, we will organize regular community meetings and workshops to educate the public about the project's progress, milestones, and achievements.

#### Documentation and Rationale: https://docs.google.com/document/d/15a6YvT4UvhR02EvyGy9EySx2RuATtXY1QHexP5FOXwk/edit?usp=sharing
