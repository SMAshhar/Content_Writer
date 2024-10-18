# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq
from agents_tasks_rbi import agents, tasks

# Types
from typing import List\

# Tools
import os
from utils import get_openai_api_key, get_serper_api_key, get_groq_api_key
from crewai_tools import (
  ScrapeWebsiteTool,
  SerperDevTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

tools: List[object] = [search_tool, scrape_tool]

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
searcher_agent=Agent(
    role=agents['idea_maker']['role'],
    goal=agents['idea_maker']['goal'],
    backstory=agents['idea_maker']['backstory'],
    verbose=agents['idea_maker']['verbose'],
    # tools=tools,
    allow_delegation=agents['idea_maker']['allow_delegation'],
    llm=llm
)
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
searching_task = Task(
    description=tasks['searching']['description'],
    expected_output=tasks['searching']['expected_output'],
    # tools=tools,
    async_execution=tasks['searching']['async_execution'],
    agent=searcher_agent
)
planning_task = Task(
    description=tasks['planning']['description'],
    expected_output=tasks['planning']['expected_output'],
    async_execution=tasks['planning']['async_execution'],
    context=[searching_task],
    agent=planner_agent
)
writing_task = Task(
    description=tasks['writing']['description'],
    expected_output=tasks['writing']['expected_output'],
    async_execution=tasks['writing']['async_execution'],
    context=[searching_task, planning_task],
    agent=writer_agent,
    output_file="./docs/final_article.md"
)


# Crew
content_writer_crew = Crew(
    agents=[searcher_agent, planner_agent, writer_agent],
    tasks=[searching_task, planning_task],
    verbose=True
)

def content_writing (
        userInput:dict=
            {
                "topic":"New Era of Starlink internet",
            }    
):
    result = content_writer_crew.kickoff(inputs=userInput)
    return result
    
content_writing()