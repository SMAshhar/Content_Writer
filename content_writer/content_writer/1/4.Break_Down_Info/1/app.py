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
info_breaker_agent=Agent(
    role=agents['breaking_down_info']['role'],
    goal=agents['breaking_down_info']['goal'],
    backstory=agents['breaking_down_info']['backstory'],
    verbose=agents['breaking_down_info']['verbose'],
    allow_delegation=agents['breaking_down_info']['allow_delegation'],
    llm=llm
)

# Tasks
breaking_down_info = Task(
    description=tasks['breaking_down_info']['description'],
    expected_output=tasks['breaking_down_info']['expected_output'],
    # tools=tasks['planning']['tools'],
    async_execution=tasks['breaking_down_info']['async_execution'],
    agent=info_breaker_agent,
    output_file="./docs/broken_down_info.csv"
)


# Crew
info_crew = Crew(
    agents=[info_breaker_agent],
    tasks=[breaking_down_info],
    verbose=True
)

with open("business_plan.md", "r") as f:
    refined_business_idea = f.read()
    # print(refined_business_idea)

with open("./docs/marketing_strategy_output.csv", "r") as f:
    marketing_strategy = f.read()
    print(marketing_strategy)

def break_down_info (
    user_input:dict=
            {
                "name":"Tea Haven",
                # "user_input":"I want to open a tea shop in California",
                "location":"California",
                # "budget":1000,
                # "plan":"I want to open a tea shop",
                "refined_business_idea":refined_business_idea,
                "marketing_strategy":marketing_strategy

            }    
):
    result = info_crew.kickoff(inputs=user_input)
    return result
    
break_down_info()