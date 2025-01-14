import pytest
from agent import SimpleMadKuduAgent

def test_research_news_invalid_company():
    agent = SimpleMadKuduAgent()
    output = agent.run({"task": "research_news", "company_name": ""})
    assert isinstance(output, str), "Expected a string for empty company_name"
    assert len(output) == 0, "Expected empty output for empty company_name"

def test_linkedin_note_missing_info():
    agent = SimpleMadKuduAgent()
    contact_info = {}
    output = agent.run({"task": "linkedin_note", "contact_info": contact_info})
    assert isinstance(output, str), "Expected a string even if contact_info is empty"
    assert "Sorry" in output, "Expected apology message for missing info"

def test_analyze_website_invalid_url():
    agent = SimpleMadKuduAgent()
    output = agent.run({"task": "analyze_website", "url": ""})
    assert isinstance(output, dict), "Expected a dict even for invalid URL"
    assert output.get("error"), "Expected 'error' key for invalid URL"

def test_firmographic_info_empty_company():
    agent = SimpleMadKuduAgent()
    output = agent.run({"task": "firmographic_info", "company_name": ""})
    assert isinstance(output, dict), "Expected a dict for empty company_name"
    assert output.get("error"), "Expected 'error' key for empty company_name"

def test_answer_company_question_empty_question():
    agent = SimpleMadKuduAgent()
    output = agent.run({"task": "answer_question", "question": "", "company_name": "SomeCorp"})
    assert isinstance(output, str), "Expected a string even if question is empty"
    assert "Sorry" in output, "Expected apology message for empty question"