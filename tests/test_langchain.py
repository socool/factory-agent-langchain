import os
from factory_agent_langchain.factory_agent_langchain import AgentMode,AgentFactory,CustomSingleAgent
from langchain.tools import Tool
from langchain import OpenAI

def test_import() -> None:
    from langchain.agents import (
        Tool,
        AgentExecutor,
        LLMSingleActionAgent,
        AgentOutputParser,
    )

    assert "import langchain passes."

def test_get_key() -> None:
    assert "check env"

def fake_func(inp: str) -> str:
    return "foo"


def test_create_single_action_agent() -> None:
    agent_mode = AgentMode.SINGLE_ACTION
    agent = AgentFactory.create_agent(agent_mode)
    assert type(agent).__name__ == "CustomSingleAgent"