# tests/test_integration.py

import pytest
from main import main
import sys
from io import StringIO


def run_main_with_args(args, monkeypatch):
    """
    Helper function to execute main.py with simulated command-line arguments.
    """
    monkeypatch.setattr(sys, 'argv', args)
    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)
    main()
    return output.getvalue().strip()


def test_main_research_news(monkeypatch):
    """
    Tests the 'research_news' task by simulating command-line arguments.
    """
    test_args = ["main.py", "--task", "research_news", "--company_name", "Microsoft"]
    result = run_main_with_args(test_args, monkeypatch)

    if "Error: Model is loading" in result:
        pytest.skip("Hugging Face model is still loading. Skipping test.")
    
    assert "Microsoft" in result, "Expected company name in research_news output"
    assert len(result) > 0, "Expected non-empty output for research_news task"


def test_main_linkedin_note_with_mock(monkeypatch, mocker):
    """
    Tests the 'linkedin_note' task by mocking the Hugging Face API response.
    """
    mocker.patch('tools.call_huggingface_api', return_value="Hi Jane Doe, I noticed your role as CTO at ExampleCorp. Let's connect!")
    test_args = [
        "main.py", "--task", "linkedin_note",
        "--contact_name", "Jane Doe",
        "--contact_role", "CTO",
        "--contact_company", "ExampleCorp"
    ]
    result = run_main_with_args(test_args, monkeypatch)

    assert "Jane Doe" in result, "Expected contact name in linkedin_note output"
    assert "CTO" in result, "Expected contact role in linkedin_note output"
    assert "ExampleCorp" in result, "Expected contact company in linkedin_note output"


def test_main_invalid_task(monkeypatch):
    """
    Tests handling of an invalid task by simulating command-line arguments.
    """
    test_args = ["main.py", "--task", "invalid_task"]
    result = run_main_with_args(test_args, monkeypatch)

    assert "Sorry, I don't recognize that task." in result, "Expected error message for invalid task"


def test_main_missing_arguments(monkeypatch):
    """
    Tests handling of missing required arguments for a task.
    """
    test_args = ["main.py", "--task", "research_news"]
    result = run_main_with_args(test_args, monkeypatch)

    assert "Error" in result or len(result) == 0, "Expected error or empty output for missing arguments"


def test_main_firmographic_info(monkeypatch):
    """
    Tests the 'firmographic_info' task by simulating command-line arguments.
    """
    test_args = ["main.py", "--task", "firmographic_info", "--company_name", "ExampleCorp"]
    result = run_main_with_args(test_args, monkeypatch)

    assert "ExampleCorp" in result, "Expected company name in firmographic_info output"
    assert "Software" in result, "Expected industry in firmographic_info output"


def test_main_answer_company_question(monkeypatch, mocker):
    """
    Tests the 'answer_question' task by mocking the Hugging Face API response.
    """
    mocker.patch('tools.call_huggingface_api', return_value="ExampleCorp specializes in cloud computing.")
    test_args = [
        "main.py", "--task", "answer_question",
        "--question", "What does the company do?",
        "--company_name", "ExampleCorp"
    ]
    result = run_main_with_args(test_args, monkeypatch)

    assert "ExampleCorp" in result, "Expected company name in answer_question output"
    assert "cloud computing" in result, "Expected generated answer in answer_question output"