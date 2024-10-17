# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq 
from agents_tasks_ba import agents, tasks


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

# Paths
from pathlib import Path
current_file_path = Path(__file__).parent


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
business_researcher=Agent(
    role=agents['business_researcher']['role'],
    goal=agents['business_researcher']['goal'],
    backstory=agents['business_researcher']['backstory'],
    verbose=agents['business_researcher']['verbose'],
    allow_delegation=agents['business_researcher']['allow_delegation'],
    llm=llm
)
budget_assigner=Agent(
    role=agents['budget_assigner']['role'],
    goal=agents['budget_assigner']['goal'],
    backstory=agents['budget_assigner']['backstory'],
    verbose=agents['budget_assigner']['verbose'],
    allow_delegation=agents['budget_assigner']['allow_delegation'],
    llm=llm
)

# Tasks
business_requirements = Task(
    description=tasks['business_requirements']['description'],
    expected_output=tasks['business_requirements']['expected_output'],
    # tools=tasks['planning']['tools'],
    async_execution=tasks['business_requirements']['async_execution'],
    agent=business_researcher
)
budget_assignment = Task(
    description=tasks['budget_assignment']['description'],
    expected_output=tasks['budget_assignment']['expected_output'],
    # tools=tasks['writing']['tools'],
    async_execution=tasks['budget_assignment']['async_execution'],
    context=[business_requirements],
    # tools=tools,
    agent=budget_assigner,
    output_file='./docs/budgetting.md'
)


# Crew
budgetting_crew = Crew(
    agents=[business_researcher, budget_assigner],
    tasks=[business_requirements, budget_assignment],
    verbose=True
)

# file_path = current_file_path / "refined_business_idea.md"
# with open("./docs/refined_business_plan.md", "r") as f:
#     refined_business_idea = f.read()
    # print(refined_business_idea)

def budget_maker (
        userInput:dict=
            {
                "name":"Zabrain's Fragrances",
                # "user_input":"I want to open a tea shop in California with a budget of 1000 usd",
                "location":"Karachi",
                # "budget":1000,
                "plan":"Perfume Impressions"
            },     
            # refined_business_idea:str=refined_business_idea
            refined_business_idea:str=""
):
    userInput.update({"refined_business_idea":refined_business_idea})
    result = budgetting_crew.kickoff(inputs=userInput)
    return result
    
# budget_maker()
# print(agents)