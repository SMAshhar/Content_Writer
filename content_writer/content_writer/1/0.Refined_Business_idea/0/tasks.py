# CrewAi
from crewai import Agent, Crew, Task
from crewai_tools import SerperDevTool, FileReadTool
from langchain_groq import ChatGroq

# Types
from types_for_task import AgentType, TaskType

# Agents
from agents import agents, agent_maker

# Tools
import os
from typing import List
from utils import get_openai_api_key, get_serper_api_key, get_groq_api_key
from crewai_tools import (
  ScrapeWebsiteTool,
  SerperDevTool
)

# environment variables
open_ai_key = get_openai_api_key()
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'
os.environ['SERPER_API_KEY'] = get_serper_api_key()

groq_ai_key = get_groq_api_key()

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=groq_ai_key
)

def task_maker(tasks:dict, agent:Agent, context:List[object]=[]):
    
    # agents_tasks={
    #     'planner': agent_maker(agents['planner'], llm=llm),
    #     'writer':agent_maker(agents['writer'], llm=llm)
    # }
    
    # selected_agent = agents_tasks[agent]
    
    task = Task(
        description=tasks['description'],
        expected_output=tasks['expected_output'],
        agent=agent,
        output_file=tasks['output_file'],
        async_execution=tasks['async_execution'],
        context=context
    )

    return task
# Task for Researcher Agent: Extract Job Requirements
tasks = {
    "planning": {
        "description":(
            "Go through the provided {user_input}. Go through each item and analyze it thoroughly "
            "use your high experience as a businees planning, asses the business idea and generate "
            "a plan to build a more complete, realistic and robust business idea "
            "if the {user_input} is unrealistic, remove the unrealistic part, give reason in paranthesis "
            "and replace with a better plan"
        ),
        "expected_output":(
            "after a thorough analysis of the business idea, budget, location from the given {user_input} "
            "a list of pointers for improved business plan with a solid base for the writer agent to  "
            "build a realistic and practical business idea"
        ),
        "agent":AgentType.PLANNER,
        "async_execution":False,
        'output_file':None
        },
    "writing":{
        "description":(
            "take in the {plan} and generate a well verced and complete business idea"
        ),
        "expected_output":(
            "a paragraph with the refined business idea"
        ),
        "agent":AgentType.WRITER,
        "async_execution":True,
        "output_file":"refined_business_idea.md"
    }
}