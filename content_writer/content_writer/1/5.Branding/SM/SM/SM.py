# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq
from agents_tasks_SM import agents, tasks


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
slogan_generator=Agent(
    role=agents['slogan_generator']['role'],
    goal=agents['slogan_generator']['goal'],
    backstory=agents['slogan_generator']['backstory'],
    verbose=agents['slogan_generator']['verbose'],
    allow_delegation=agents['slogan_generator']['allow_delegation'],
    llm=llm
)

# Tasks
slogan_generating = Task(
    description=tasks['slogan_generation']['description'],
    expected_output=tasks['slogan_generation']['expected_output'],
    # tools=tasks['planning']['tools'],
    async_execution=tasks['slogan_generation']['async_execution'],
    agent=slogan_generator,
    output_file="./docs/slogans.md"
)


# Crew
slogan_crew = Crew(
    agents=[slogan_generator],
    tasks=[slogan_generating],
    verbose=True
)

# refined_business_idea_path = current_file_path / "refined_business_idea.md"
# with open(refined_business_idea_path, "r") as f:
#     refined_business_idea = f.read()
    # print(refined_business_idea)

# broken_down_info_path = current_file_path / "docs/broken_down_info.csv"
# with open(broken_down_info_path, "r") as f:
#     broken_down_info = f.read()
#     print(broken_down_info)

def slogan_maker (
    userInput:dict=
            {
                "name":"Zabrain's Fragrances",
                # "user_input":"I want to open a tea shop in California with a budget of 1000 usd",
                "location":"Karachi",
                # "budget":1000,
                "plan":"Perfume Impressions"
            },     
            # broken_down_info:str=broken_down_info
            broken_down_info:str=""
):
    userInput.update({"broken_down_info":broken_down_info})
    result = slogan_crew.kickoff(inputs=userInput)
    return result
    
# slogan_maker()