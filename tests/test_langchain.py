import os

def test_import() -> None:
    from langchain.agents import (
        Tool,
        AgentExecutor,
        LLMSingleActionAgent,
        AgentOutputParser,
    )

    assert "import langchain passes."

def test_get_key() -> None:
    print(">>>",os.environ.get('SERPAPI_API_KEY'))
    assert "check env"