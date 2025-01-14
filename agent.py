from typing import Union
from tools import (
    find_relevant_news,
    generate_linkedin_note,
    analyze_website,
    get_firmographic_info,
    answer_company_question
)

class SimpleMadKuduAgent:
    """
    Simple agent that decides which 'tool' function to call based on a user's task.
    """

    def run(self, user_input: dict) -> Union[str, dict]:
        task = user_input.get("task")

        if task == "research_news":
            company = user_input.get("company_name", "")
            return find_relevant_news(company)

        elif task == "linkedin_note":
            contact_info = user_input.get("contact_info", {})
            return generate_linkedin_note(contact_info)

        elif task == "analyze_website":
            url = user_input.get("url", "")
            return analyze_website(url)

        elif task == "firmographic_info":
            company = user_input.get("company_name", "")
            return get_firmographic_info(company)

        elif task == "answer_question":
            question = user_input.get("question", "")
            company = user_input.get("company_name", "")
            return answer_company_question(question, company)

        else:
            return "Sorry, I don't recognize that task."