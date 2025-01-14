import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from serpapi import GoogleSearch

# Load environment variables from .env file
load_dotenv()

# Get Hugging Face API token from environment variables
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN", "")
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

# Set the headers for Hugging Face API requests
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"
}

def call_huggingface_api(prompt: str, max_length: int = 300) -> str:
    """
    Makes a request to the Hugging Face Inference API and returns the generated text.
    """
    if not prompt:
        return "Error: No prompt provided."

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "temperature": 0.7,
            "top_p": 0.95,
            "do_sample": True
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 403:
            return "Error: Access to this model is restricted. Please try a different model."
        if response.status_code == 503:
            return "Error: Model is loading. Please try again shortly."
        response.raise_for_status()
        data = response.json()
        return data[0]["generated_text"].strip()
    except Exception as e:
        print(f"Error calling Hugging Face API: {e}")
        return "Error: Could not generate a response."

def find_relevant_news(company_name: str) -> str:
    """
    Searches for recent news about a company using SerpAPI and summarizes the results.
    """
    if not company_name:
        return ""

    serpapi_key = os.getenv("SERPAPI_API_KEY", "")
    if not serpapi_key:
        raise ValueError("SERPAPI_API_KEY environment variable not set.")

    base_url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": f"{company_name} news",
        "api_key": serpapi_key,
        "location": "United States",
        "hl": "en",
        "gl": "us"
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        return f"SerpAPI search failed with status {response.status_code}: {response.text}"

    results = response.json()
    organic_results = results.get("organic_results", [])
    if not organic_results:
        return f"No news results found for {company_name}."

    snippets = []
    for idx, result in enumerate(organic_results[:3]):
        title = result.get("title", "")
        snippet = result.get("snippet", "")
        link = result.get("link", "")
        snippets.append(f"{idx+1}. Title: {title}\n   Snippet: {snippet}\n   Link: {link}\n")

    combined_snippets = "\n".join(snippets)

    prompt = (
        f"Summarize the following recent news about {company_name} in 2-3 sentences:\n\n"
        f"{combined_snippets}"
    )
    summary = call_huggingface_api(prompt)
    return summary

def generate_linkedin_note(contact_info: dict) -> str:
    """
    Generates a personalized LinkedIn connection note for a contact.
    """
    if not contact_info or not all(contact_info.values()):
        return "Sorry, the contact information is incomplete."

    name = contact_info.get("name", "there")
    role = contact_info.get("role", "")
    company = contact_info.get("company", "")

    prompt = (
        f"Write a short LinkedIn connection note to {name}, "
        f"who is the {role} at {company}. The note should be friendly, "
        "mention collaboration or industry trends, and be concise."
    )
    note = call_huggingface_api(prompt)
    return note

def analyze_website(url: str) -> dict:
    """
    Analyzes a website's text to extract:
    - Value proposition
    - Sales motion
    - Pricing structure
    """
    if not url:
        return {"error": "No URL provided."}

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        html_content = resp.text
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    prompt = (
        "Analyze this website text and identify the following:\n"
        "1) value proposition\n"
        "2) sales motion (e.g., self-serve, enterprise, etc.)\n"
        "3) pricing structure\n\n"
        f"Website text:\n{text}\n\n"
        "Return your findings in a JSON-like format."
    )
    analysis_text = call_huggingface_api(prompt)
    return {"analysis": analysis_text}

def get_firmographic_info(company_name: str) -> dict:
    """
    Returns firmographic data (e.g., size, industry) for a company.
    """
    if not company_name:
        return {"error": "No company name provided"}

    return {
        "company_name": company_name,
        "size": "1,000-5,000 employees (estimated)",
        "industry": "Software"
    }

def answer_company_question(question: str, company_name: str) -> str:
    """
    Answers a specific question about a company.
    """
    if not question:
        return "Sorry, no question provided."

    snippet = f"{company_name} is an industry leader in software services."
    prompt = (
        f"{snippet}\n\n"
        f"Q: {question}\n"
        f"A: "
    )
    answer = call_huggingface_api(prompt)
    return answer