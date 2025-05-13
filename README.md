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

