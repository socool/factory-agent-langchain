from langchain.agents import Tool, BaseSingleActionAgent
from langchain import SerpAPIWrapper

from langchain.utilities import SerpAPIWrapper

from typing import List, Tuple, Any, Union
from langchain.schema import AgentAction, AgentFinish
from langchain.agents.agent_types import AgentType

from enum import Enum

search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
        return_direct=True,
    )
]

class CustomSingleAgent(BaseSingleActionAgent):
    """Fake Custom Agent."""

    @property
    def _agent_type(self) -> str:
        """Return Identifier of agent type."""
        return AgentType.ZERO_SHOT_REACT_DESCRIPTION

    @property
    def input_keys(self):
        return ["input"]

    def plan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")

    async def aplan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")
    
class CustomMultiAgent(BaseSingleActionAgent):
    """Fake Custom Agent."""

    @property
    def input_keys(self):
        return ["input"]

    def plan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")

    async def aplan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")

class AgentMode(Enum):
    SINGLE_ACTION = "SINGLE_ACTION"
    MULTI_ACTION = "MULTI_ACTION"

class AgentFactory:
    @staticmethod
    def create_agent(agent_mode: AgentMode, **kwargs: Any) -> BaseSingleActionAgent:
        # Determine the specific agent subclass based on the provided parameters
        if agent_mode.SINGLE_ACTION:
            agent = CustomSingleAgent()
        elif agent_mode.MULTI_ACTION:
            agent = CustomMultiAgent()
        else:
            raise ValueError("Invalid parameters for creating the agent.")

        return agent