# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq
from agents_tasks_rbi import agents, tasks

# Types
from typing import List
from types_for_crew import BusinessIdeaAgent

# Tools
import os
from utils import get_openai_api_key, get_serper_api_key, get_groq_api_key
# from crewai_tools import (
#   ScrapeWebsiteTool,
#   SerperDevTool
# )

# search_tool = SerperDevTool()
# scrape_tool = ScrapeWebsiteTool()

# tools: List[object] = [scrape_tool, search_tool]

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
planner_agent=Agent(
    role=agents['planner']['role'],
    goal=agents['planner']['goal'],
    backstory=agents['planner']['backstory'],
    verbose=agents['planner']['verbose'],
    allow_delegation=agents['planner']['allow_delegation'],
    llm=llm
)
writer_agent=Agent(
    role=agents['writer']['role'],
    goal=agents['writer']['goal'],
    backstory=agents['writer']['backstory'],
    verbose=agents['writer']['verbose'],
    allow_delegation=agents['writer']['allow_delegation'],
    llm=llm
)

# Tasks
planning_task = Task(
    description=tasks['planning']['description'],
    expected_output=tasks['planning']['expected_output'],
    # tools=tasks['planning']['tools'],
    async_execution=tasks['planning']['async_execution'],
    agent=planner_agent
)
writing_task = Task(
    description=tasks['writing']['description'],
    expected_output=tasks['writing']['expected_output'],
    # tools=tasks['writing']['tools'],
    async_execution=tasks['writing']['async_execution'],
    context=[planning_task],
    agent=writer_agent,
    output_file='./docs/refined_business_plan.md'
)


# Crew
RefinedBusinessIdeaCrew = Crew(
    agents=[planner_agent, writer_agent],
    tasks=[planning_task, writing_task],
    verbose=True
)

def refined_business_idea (
        userInput:dict=
            {
                "name":"Zabrain's Fragrances",
                # "user_input":"I want to open a tea shop in California with a budget of 1000 usd",
                "location":"Karachi",
                # "budget":1000,
                "plan":"Perfume Impressions"
            }    
):
    result = RefinedBusinessIdeaCrew.kickoff(inputs=userInput)
    return result
    
# refined_business_idea()