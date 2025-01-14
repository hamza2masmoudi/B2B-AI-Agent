# main.py

import argparse
from agent import SimpleMadKuduAgent

def main():
    parser = argparse.ArgumentParser(description="MadKudu-Like Agent CLI")
    parser.add_argument("--task", type=str, required=True, help="Task to perform")
    parser.add_argument("--company_name", type=str, default="")
    parser.add_argument("--url", type=str, default="")
    parser.add_argument("--question", type=str, default="")
    parser.add_argument("--contact_name", type=str, default="")
    parser.add_argument("--contact_role", type=str, default="")
    parser.add_argument("--contact_company", type=str, default="")

    args = parser.parse_args()
    agent = SimpleMadKuduAgent()

    # Build the user_input dictionary
    user_input = {"task": args.task}

    if args.company_name:
        user_input["company_name"] = args.company_name
    if args.url:
        user_input["url"] = args.url
    if args.question:
        user_input["question"] = args.question
    if args.contact_name or args.contact_role or args.contact_company:
        user_input["contact_info"] = {
            "name": args.contact_name,
            "role": args.contact_role,
            "company": args.contact_company
        }

    result = agent.run(user_input)
    print(result)

if __name__ == "__main__":
    main()