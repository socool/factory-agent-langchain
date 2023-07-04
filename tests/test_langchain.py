def test_import() -> None:
    from langchain.agents import (
        Tool,
        AgentExecutor,
        LLMSingleActionAgent,
        AgentOutputParser,
    )

    assert "import langchain passes."