from typing import List, TypedDict
from crewai import Agent
from langchain_groq import ChatGroq
from enum import Enum

class BusinessInput(TypedDict):
    business_name: str
    business_idea: str
    location: str
    budget: str

class CrewaiAgent:
    def __init__(self, agent_name: str, agent_role: str, agent_goals: str, agent_backstory: str, tools: List[object], llm: ChatGroq):
        self.name = agent_name
        self.role = agent_role
        self.goal = agent_goals
        self.backstory = agent_backstory
        self.verbose = True
        self.llm = llm
        self.tools = tools
    
    def get_agent(self):
        return Agent(
            name=self.name,
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            verbose=self.verbose,
            llm=self.llm,
            tools=self.tools
        )

class BusinessIdeaAgent(TypedDict):
    role: str
    goal: str
    backstory: str
    verbose: bool
    tools: List[object]  # Assuming scrape_tool and search_tool are objects of some tool classes
    allow_delegation: bool
    
class AgentType(Enum):
    PLANNER="planner"
    WRITER="writer"
    
class Task():
    description:str
    expected_output:str
    agent:Agent
    async_execution:bool
    context:List[object]
    
class TaskType(Enum):
    PLANNING="planning"
    WRITING="writing"