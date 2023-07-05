from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent
from langchain import OpenAI, SerpAPIWrapper

# Abstract course
class Course:
 
    def __init__(self):
        self.Fee()
        self.available_batches()
 
    def Fee(self):
        raise NotImplementedError
 
    def available_batches(self):
        raise NotImplementedError
 
    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)
 
# concrete course
class DSA(Course):
 
    """Class for Data Structures and Algorithms"""
 
    def Fee(self):
        self.fee = 8000
 
    def available_batches(self):
        self.batches = 5
 
    def __str__(self):
        return "DSA"
 
# concrete course
class SDE(Course):
 
    """Class for Software Development Engineer"""
 
    def Fee(self):
        self.fee = 10000
 
    def available_batches(self):
        self.batches = 4
 
    def __str__(self):
        return "SDE"
 
# concrete course
class STL(Course):
 
    """Class for Standard Template Library"""
 
    def Fee(self):
        self.fee = 5000
 
    def available_batches(self):
        self.batches = 7
 
    def __str__(self):
        return "STL"
 
# Complex Course
class ComplexCourse:
 
    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)
 
# Complex course
class Complexcourse(ComplexCourse):
 
    def Fee(self):
        self.fee = 7000
 
    def available_batches(self):
        self.batches = 6
 
# construct course
def construct_course(cls):
 
    course = cls()
    course.Fee()
    course.available_batches()
 
    return course    # return the course object
 
# main method
if __name__ == "__main__":
 
    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course
    stl = STL()  # object for STL course
 
    complex_course = construct_course(Complexcourse)
    print(complex_course)

from langchain.utilities import SerpAPIWrapper

search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
        return_direct=True,
    )
]

from typing import List, Tuple, Any, Union,Sequence
from langchain.schema import AgentAction, AgentFinish
from langchain.agents.agent_types import AgentType
from langchain.base_language import BaseLanguageModel
from langchain.tools.base import BaseTool

from enum import Enum

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