# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq
from agents_tasks_p import agents, tasks


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
government_policy_extractor=Agent(
    role=agents['government_policy_extractor']['role'],
    goal=agents['government_policy_extractor']['goal'],
    backstory=agents['government_policy_extractor']['backstory'],
    verbose=agents['government_policy_extractor']['verbose'],
    allow_delegation=agents['government_policy_extractor']['allow_delegation'],
    llm=llm
)
company_policy_strategist=Agent(
    role=agents['company_policy_strategist']['role'],
    goal=agents['company_policy_strategist']['goal'],
    backstory=agents['company_policy_strategist']['backstory'],
    verbose=agents['company_policy_strategist']['verbose'],
    allow_delegation=agents['company_policy_strategist']['allow_delegation'],
    llm=llm
)

company_policy_writer=Agent(
    role=agents['company_policy_writer']['role'],
    goal=agents['company_policy_writer']['goal'],
    backstory=agents['company_policy_writer']['backstory'],
    verbose=agents['company_policy_writer']['verbose'],
    allow_delegation=agents['company_policy_writer']['allow_delegation'],
    llm=llm
)

# Tasks
policy_extraction = Task(
    description=tasks['policy_extraction']['description'],
    expected_output=tasks['policy_extraction']['expected_output'],
    # tools=tasks['planning']['tools'],
    async_execution=tasks['policy_extraction']['async_execution'],
    agent=government_policy_extractor,
    output_file="./docs/gov_policy_output.csv"
)
strategy_layout = Task(
    description=tasks['strategy_layout']['description'],
    expected_output=tasks['strategy_layout']['expected_output'],
    # tools=tasks['writing']['tools'],
    async_execution=tasks['strategy_layout']['async_execution'],
    context=[policy_extraction],
    # tools=tools,
    agent=company_policy_strategist,
    output_file='./docs/strategy_layout_output.csv'
)
company_policy_document = Task(
    description=tasks['company_policy_document']['description'],
    expected_output=tasks['company_policy_document']['expected_output'],
    # tools=tasks['writing']['tools'],
    async_execution=tasks['company_policy_document']['async_execution'],
    context=[policy_extraction, strategy_layout],
    # tools=tools,
    agent=company_policy_writer,
    output_file='./docs/company_policy_document_output.md'
)


# Crew
marketing_crew = Crew(
    agents=[government_policy_extractor, company_policy_strategist, company_policy_writer],
    tasks=[policy_extraction, strategy_layout, company_policy_document],
    verbose=True
)


# file_path = current_file_path / "refined_business_idea.md"
# with open(file_path, "r") as f:
#     refined_business_idea = f.read()
    # print(refined_business_idea)

# with open("budgeting.csv", "r") as f:
#     budgeting = f.read()
    # print(budgeting)

def business_policies (
    user_input:dict=
            {
                "name":"Zabrain's Fragrances",
                # "user_input":"I want to open a tea shop in California with a budget of 1000 usd",
                "location":"Karachi",
                # "budget":1000,
                "plan":"Perfume Impressions"
            },    
                # refined_business_idea=refined_business_idea,
                refined_business_idea:str="",
):
    user_input.update({"refined_business_idea":refined_business_idea})
    result = marketing_crew.kickoff(inputs=user_input)
    return result
    
# business_policies()