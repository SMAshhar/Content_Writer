# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq
from agents_tasks import agents, tasks


# Types
from typing import List
from types_for_crew import BusinessIdeaAgent

# Tools
import os
from utils import get_openai_api_key, get_serper_api_key, get_groq_api_key
from crewai_tools import (
  ScrapeWebsiteTool,
  SerperDevTool
)

search_tool = SerperDevTool(
    search_url="https://google.serper.dev/scholar",
    n_results=2,
)
scrape_tool = ScrapeWebsiteTool()

tools: List[object] = [scrape_tool, search_tool]

# environment variables
open_ai_key = get_openai_api_key()
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'
os.environ['SERPER_API_KEY'] = get_serper_api_key()

groq_ai_key = get_groq_api_key()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=groq_ai_key
)

# Agents
market_researcher=Agent(
    role=agents['market_researcher']['role'],
    goal=agents['market_researcher']['goal'],
    backstory=agents['market_researcher']['backstory'],
    verbose=agents['market_researcher']['verbose'],
    allow_delegation=agents['market_researcher']['allow_delegation'],
    llm=llm
)
marketing_planner=Agent(
    role=agents['marketing_planner']['role'],
    goal=agents['marketing_planner']['goal'],
    backstory=agents['marketing_planner']['backstory'],
    verbose=agents['marketing_planner']['verbose'],
    allow_delegation=agents['marketing_planner']['allow_delegation'],
    llm=llm
)

marketing_strategy_developer=Agent(
    role=agents['marketing_strategy_developer']['role'],
    goal=agents['marketing_strategy_developer']['goal'],
    backstory=agents['marketing_strategy_developer']['backstory'],
    verbose=agents['marketing_strategy_developer']['verbose'],
    allow_delegation=agents['marketing_strategy_developer']['allow_delegation'],
    llm=llm
)

# Tasks
market_research = Task(
    description=tasks['market_research']['description'],
    expected_output=tasks['market_research']['expected_output'],
    # tools=tasks['planning']['tools'],
    async_execution=tasks['market_research']['async_execution'],
    agent=market_researcher,
    output_file="./docs/market_research_output.csv"
)
marketing_planning = Task(
    description=tasks['marketing_planning']['description'],
    expected_output=tasks['marketing_planning']['expected_output'],
    # tools=tasks['writing']['tools'],
    async_execution=tasks['marketing_planning']['async_execution'],
    context=[market_research],
    # tools=tools,
    agent=marketing_planner,
    output_file='./docs/marketing_planning_output.csv'
)
strategy_development = Task(
    description=tasks['strategy_development']['description'],
    expected_output=tasks['strategy_development']['expected_output'],
    # tools=tasks['writing']['tools'],
    async_execution=tasks['strategy_development']['async_execution'],
    context=[market_research, marketing_planning],
    # tools=tools,
    agent=marketing_strategy_developer,
    output_file='./docs/marketing_strategy_output.md'
)


# Crew
marketing_crew = Crew(
    agents=[market_researcher, marketing_planner, marketing_strategy_developer],
    tasks=[market_research, marketing_planning, strategy_development],
    verbose=True
)

with open("business_plan.md", "r") as f:
    refined_business_idea = f.read()
    # print(refined_business_idea)

with open("budgeting.csv", "r") as f:
    budgeting = f.read()
    # print(budgeting)

def marketing_strategy (
        user_input:dict=
            {
        # "user_input":"I want to open a tea shop in California",
        "location":"Karachi",
        # "budget":1000,
        "plan":"I want to open a tea shop",
        "refined_business_idea":refined_business_idea,
        "budgeting":budgeting

    }    
):
    result = marketing_crew.kickoff(inputs=user_input)
    return result
    
marketing_strategy()