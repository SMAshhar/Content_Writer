# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq

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

search_tool = SerperDevTool()
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

def agent_maker(agent:BusinessIdeaAgent, llm:ChatGroq):
    agent = Agent(
        role=agent["role"],
        goal=agent["goal"],
        tools=agent["tools"],
        verbose=agent["verbose"],
        backstory=agent["backstory"],
        allow_delegation=agent["allow_delegation"],
        llm=llm,
    )
    return agent
# Agents
# Agent 1: Business Model Planner
agents: dict[str, BusinessIdeaAgent] = {
    "planner":{
        "role":"Business Planner",
        "goal":("Make sure to do amazing analysis on the given business idea "
            "find the things that are missing for it to be a viable business idea "
            "and list down all the points necessary to make the business a really "
            "successful one. output in pointers"),
        "tools" : [],
        "verbose":True,
        "backstory":(
            "as an expert business planner, your prowess in "
            "studying the business idea provided to you "
            "taking in critical points and develop an awesome "
            "business plan is unmatched."
            "Your skills help pinpoint the necessary "
            "things that were not mentioned in the idea, "
            "combine them with the business idea and generate "
            "a more complete business idea."
        ),
        'allow_delegation':False
        # "llm":llm
    },
    "writer":{
        "role":"Business Idea Writer",
        "goal":("take in the data from business planner and develop "
            "a fully detailed, complete and practical business plan "
            "with respect to the location, the budget and the name "
            "then brief it down to 5 - 6 lines"
            ),
        "tools" : [],
        "verbose":True,
        "backstory":(
            "as an expert business man, your prowess in "
            "studying the business idea provided to you "
            "studying through the critical points and develop an awesome "
            "business plan is unmatched."
            "Your skills help take in all the necessary points in "
            "a business plan and write down clearly in a buisness yet easily-understandable "
            "writeup"
        ),
        'allow_delegation':False
        # "llm":llm
    },
    # "checker":{
    #     "role":"Business Ide",
    #     "goal":("take in the data from business planner and make "
    #         "and make that business idea into a full flash business plan"
    #         "write a paragraph with the improved and complete buiness idea"),
    #     "tools" : [scrape_tool, search_tool],
    #     "verbose":True,
    #     "backstory":(
    #         "as an expert business planner, your prowess in "
    #         "studying the business idea provided to you "
    #         "taking in critical points and develop an awesome "
    #         "business plan is unmatched."
    #         "Your skills help pinpoint the necessary "
    #         "things that were not mentioned in the idea, "
    #         "combine them with the business idea and generate "
    #         "a more complete business idea."
    #     ),
    #     "llm":llm
    # },
}

print(type(llm))