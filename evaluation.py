# evaluation.py

from agent import SimpleMadKuduAgent

def evaluate_news_relevance():
    agent = SimpleMadKuduAgent()
    company_name = "Microsoft"
    output = agent.run({"task": "research_news", "company_name": company_name})
    # Simulated relevance evaluation: check for the company's name in output
    relevant_score = output.lower().count(company_name.lower()) / len(output.split())
    print(f"News relevance score for {company_name}: {relevant_score:.2f}")

def evaluate_linkedin_notes():
    agent = SimpleMadKuduAgent()
    contact_info = {"name": "Jane Doe", "role": "CTO", "company": "ExampleCorp"}
    output = agent.run({"task": "linkedin_note", "contact_info": contact_info})
    # Simulated user rating based on key mentions
    ideal_mentions = [contact_info["name"], contact_info["role"], contact_info["company"]]
    relevance_score = sum(1 for mention in ideal_mentions if mention in output) / len(ideal_mentions)
    print(f"LinkedIn note relevance score: {relevance_score:.2f}")

def evaluate_website_analysis():
    agent = SimpleMadKuduAgent()
    url = "https://www.example.com"
    output = agent.run({"task": "analyze_website", "url": url})
    # Simulated check for relevant keys
    expected_keys = ["value_proposition", "sales_motion", "pricing"]
    precision_score = sum(1 for key in expected_keys if key in output.get("analysis", "")) / len(expected_keys)
    print(f"Website analysis precision score: {precision_score:.2f}")

if __name__ == "__main__":
    evaluate_news_relevance()
    evaluate_linkedin_notes()
    evaluate_website_analysis()