## My Ai Agent

This is a simple AI Agent that can:
1. Research B2B accounts to identify relevant news.
2. Write a personal LinkedIn note given a contact's information.
3. Explore a website to understand a company's value proposition, sales motion, and pricing structure.
4. Research companies to get firmographic information (company size, industry).
5. Answer questions about a company by searching the web and/or scraping.

## Requirements

- Python 3.8+
- A Hugging Face API key for text generation.
- A SerpAPI key for fetching real-time search results.

## Installation

1. Clone this repository (or download the folder you’ve created).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt


3.	Set up environment variables in a .env file:
HUGGINGFACE_API_TOKEN=your_huggingface_api_token
SERPAPI_API_KEY=your_serpapi_api_key

Replace your_huggingface_api_token and your_serpapi_api_key with valid API keys.

## Usage

To run the agent, use:

python main.py --task <TASK> [other arguments]

# Available Tasks and Arguments

Task              | Required Arguments                         | Example
------------------|--------------------------------------------|----------------------------------------------------------------------------------
research_news     | --company_name                             | python main.py --task research_news --company_name Microsoft
linkedin_note     | --contact_name, --contact_role, --contact_company | python main.py --task linkedin_note --contact_name "Jane Doe" --contact_role "CTO" --contact_company "ExampleCorp"
analyze_website   | --url                                      | python main.py --task analyze_website --url "https://www.example.com"
firmographic_info | --company_name                             | python main.py --task firmographic_info --company_name Google
answer_question   | --question, --company_name                 | python main.py --task answer_question --question "What does the company do?" --company_name Amazon


## Testing

To run all tests:

PYTHONPATH=$(pwd) pytest tests


## Project Structure 

| File/Folder         | Description                                       |
|---------------------|---------------------------------------------------|
| main.py             | Command-line interface for the agent             |
| agent.py            | Core agent logic for task routing                |
| tools.py            | Implementation of individual task functions      |
| tests/              | Unit and integration tests                       |
| ├── test_agent.py   | Unit tests                                       |
| ├── test_integration.py | Integration tests                           |
| requirements.txt    | Python dependencies                              |
| README.md           | Project documentation                            |
| .env                | Environment variables (not included in the repo) |
## Future Enhancements


	•	Add retry logic for handling API loading issues.
	•	Integrate more robust firmographic data APIs like Clearbit or Crunchbase.
	•	Fine-tune prompts for improved accuracy.


## Author

	•	Developed by Hamza Masmoudi
