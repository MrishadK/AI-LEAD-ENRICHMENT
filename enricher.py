import os
import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_with_gemini(company_name):
    """Use Gemini's knowledge to generate company insights without external data."""
    prompt = f"""
    You are an AI business analyst. Provide comprehensive information about {company_name} based on your existing knowledge.
    
    Provide the following details:
    1. Most likely website domain (just the domain name)
    2. A concise 2-3 sentence summary of what the company does
    3. The company's primary industry/sector
    4. Estimated company size (employee range)
    5. Headquarters location
    6. The company's likely target customer profile
    7. An AI automation idea that could benefit this company
    
    Format your response exactly like this:
    Website: [domain.com]
    Summary: [summary text]
    Industry: [industry]
    Size: [employee range]
    Location: [headquarters]
    Target: [target customers]
    Idea: [AI automation idea]
    """
    
    try:
        response = model.generate_content(prompt)
        return parse_gemini_response(response.text)
    except Exception as e:
        print(f"Gemini error analyzing {company_name}: {e}")
        return default_response()

def parse_gemini_response(text):
    """Parse Gemini's structured response."""
    result = default_response()
    current_field = None
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("Website:"):
            current_field = "website"
            result["website"] = line.replace("Website:", "").strip()
        elif line.startswith("Summary:"):
            current_field = "summary"
            result["summary"] = line.replace("Summary:", "").strip()
        elif line.startswith("Industry:"):
            current_field = "industry"
            result["industry"] = line.replace("Industry:", "").strip()
        elif line.startswith("Size:"):
            current_field = "size"
            result["size"] = line.replace("Size:", "").strip()
        elif line.startswith("Location:"):
            current_field = "location"
            result["location"] = line.replace("Location:", "").strip()
        elif line.startswith("Target:"):
            current_field = "target"
            result["target"] = line.replace("Target:", "").strip()
        elif line.startswith("Idea:"):
            current_field = "idea"
            result["idea"] = line.replace("Idea:", "").strip()
        elif current_field:
            result[current_field] += " " + line
            
    return result

def default_response():
    """Return default empty response structure."""
    return {
        "website": "N/A",
        "summary": "Could not analyze company",
        "industry": "N/A",
        "size": "N/A",
        "location": "N/A",
        "target": "N/A",
        "idea": "N/A"
    }

def enrich_companies(input_csv="input.csv"):
    """Main function to process company list."""
    df = pd.read_csv(input_csv)
    results = []

    for _, row in df.iterrows():
        company = row["company_name"]
        print(f"\n🔎 Analyzing: {company}")
        
        analysis = analyze_with_gemini(company)
        
        results.append({
            "company_name": company,
            "website": analysis["website"],
            "summary": analysis["summary"],
            "industry": analysis["industry"],
            "company_size": analysis["size"],
            "location": analysis["location"],
            "target_customer": analysis["target"],
            "automation_idea": analysis["idea"]
        })

    output_df = pd.DataFrame(results)
    output_path = "output_enriched.csv"
    output_df.to_csv(output_path, index=False)
    print(f"\n✅ Done! Output saved to {output_path}")
    return output_path

if __name__ == "__main__":
    enrich_companies()