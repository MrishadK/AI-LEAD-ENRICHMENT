# AI-Powered Lead Enrichment Bot

**Lead Enrichment Bot Demo**  


https://github.com/user-attachments/assets/7ab26cce-fc94-4b84-9d9f-0dadb119505f


---

## Overview

This AI-powered tool automatically enriches company lead data using Google's Gemini AI. Simply upload a CSV with company names and receive detailed profiles including websites, industry information, company size, and AI automation ideas.

---

## ✨ Features
  
- **⚡ AI-Powered Insights:** Leverages Gemini 1.5 Flash for precise and actionable company analysis.
- **📊 7 Key Data Points:** Extracts website, summary, industry, size, location, target customers, and automation ideas.
- **💻 Simple Interface:** Built on Streamlit , offering an intuitive web app for seamless uploads and downloads.
- **📂 Batch Processing:** Handles multiple companies in a single CSV file for efficient enrichment.
---

## Setup Instructions

-  **Clone the repository:**

```bash
git clone https://github.com/MrishadK/AI-LEAD-ENRICHMENT.git
cd ai-lead-enrichment
```

- **Install dependencies:**

```bash
pip install -r requirements.txt
```

- **Set up environment variables:**

Create a .env file in the root directory
Add your Gemini API key:

```ini
GEMINI_API_KEY=your_api_key_here
```
- **Run the application:**
```bash
streamlit run app.py
```

### Usage
- Prepare a CSV file with a column named company_name containing the companies you want to analyze
- Upload the CSV through the web interface
- Click Run Enrichment to process the data
- Download the enriched CSV with all additional fields


### Sample Input & Output

**Sample Input (input.csv):**
```csv
company_name
OpenAI
DeepMind
Zoho
Freshworks
```

**Sample Output (output_enriched.csv):**
```csv
company_name,website,summary,industry,company_size,location,target_customer,automation_idea
OpenAI,openai.com,"OpenAI is a leading artificial intelligence research company developing and deploying advanced AI technologies, including large language models like GPT, to benefit humanity.  They offer various APIs and tools for developers and businesses to integrate AI capabilities into their applications and services.",Artificial Intelligence (AI) / Software as a Service (SaaS),300-500 employees (estimated),"San Francisco, California","Developers, businesses (across various sectors needing AI capabilities), researchers, and individuals interested in AI technology.","An AI-powered system for automated research paper analysis and summarization. This system would ingest research papers related to AI advancements, extract key findings, summarize the papers' conclusions, and identify potential collaborations or areas for further research, thus significantly accelerating OpenAI's internal research processes and knowledge acquisition."
DeepMind,deepmind.com,"DeepMind is a leading artificial intelligence company that develops advanced algorithms and applies them to a wide range of challenges, including scientific research, healthcare, and game playing.  Their work focuses on creating general-purpose AI with the potential to solve real-world problems.","Artificial Intelligence, Technology",1000-2500 employees,"London, England","Businesses seeking AI solutions for complex problems, scientific research institutions, healthcare providers, and technology companies.","An AI-powered system to automate the process of identifying and prioritizing research opportunities within DeepMind's vast dataset of research papers, publications, and internal projects. This system could analyze existing work, predict future research directions, and suggest optimal collaborations, significantly improving research efficiency and innovation."
Zoho,zoho.com,"Zoho provides a comprehensive suite of cloud-based business applications, including CRM, email, project management, and more, designed to help businesses of all sizes manage their operations.  Their focus is on providing affordable and integrated solutions to improve productivity and collaboration.","Software as a Service (SaaS), Cloud Computing","10,000 - 15,000 employees","Pleasanton, California, USA","Small and medium-sized businesses (SMBs), enterprises, and individual entrepreneurs needing integrated business tools.  They also cater to specific industry needs with tailored solutions.","An AI-powered predictive customer churn model integrated across all Zoho applications.  This model would analyze user behavior and predict which customers are at risk of leaving, allowing proactive intervention through targeted customer support, personalized offers, and tailored communication strategies."
Freshworks,freshworks.com,"Freshworks provides a suite of cloud-based customer service and engagement software solutions, helping businesses of all sizes improve customer relationships and streamline operations.  Their products range from CRM and helpdesk to marketing automation and communication tools.","Customer Relationship Management (CRM) Software, SaaS (Software as a Service)",5000-10000 employees (estimate based on various sources),"San Mateo, California, USA","Businesses of all sizes, from small and medium-sized enterprises (SMEs) to large corporations, seeking to improve customer experience and operational efficiency through software solutions.  Specifically, businesses that need helpdesk, CRM, marketing automation, and communication tools.","An AI-powered predictive churn model integrated across all Freshworks products. This model would analyze customer interaction data (tickets, emails, calls, engagement with marketing materials) to identify at-risk customers and proactively suggest interventions like personalized offers or prioritized support, leading to improved customer retention and increased revenue."
```

### Tools & Technologies
- Python 3.10.0
- Streamlit - Web application framework
- Google Gemini API - AI model for company analysis
- Pandas - Data processing and CSV handling
- python-dotenv - Environment variable management
