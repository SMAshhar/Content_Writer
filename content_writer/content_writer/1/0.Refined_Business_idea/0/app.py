# GenAI
from crewai import Crew, Agent, Task
from langchain_groq import ChatGroq

#Types
from typing import List
from types_for_task import AgentType, TaskType

# Agent and task
import os
from agents import agents, agent_maker
from tasks import tasks, task_maker

from utils import get_groq_api_key, get_openai_api_key, get_serper_api_key

groq_ai_key = get_groq_api_key()

open_ai_key = get_openai_api_key()
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4o'
os.environ['SERPER_API_KEY'] = get_serper_api_key()

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    api_key=groq_ai_key
)

print(tasks)
def crew_maker(agents_objects:List[AgentType], tasks_objects:List[TaskType], llm:ChatGroq, verbose:bool=True):
    
    planner = agent_maker(agents_objects['planner'], llm=llm)
    writer = agent_maker(agents_objects['writer'], llm=llm)

    # print("agents for crew",agents_for_crew)
    # tasks_for_crew=[
    #     task_maker(tasks_objects['planning'], "planner"), 
    #     task_maker(tasks_objects['writing'], 'writer')
    # ]

    planning = task_maker(tasks_objects['planning'], planner)
    writing = task_maker(tasks_objects['writing'], writer, [planning])
    crew = Crew(
        agents=[planner, writer],
        tasks=[planning, writing],
        verbose=verbose
    )
    return crew

def agent_refined_business_idea(user_input:object):
    
    businessIdeaCrew = crew_maker(
        agents_objects=agents,
        tasks_objects=tasks,
        llm=llm,
        verbose=False
    )

    result = businessIdeaCrew.kickoff(inputs=user_input)
    
    print(result)
    
    return result

agent_refined_business_idea({
        "user_input":"I want to open a tea shop in California with a budget of 1000 usd",
        "location":"California",
        "budget":1000,
        "plan":"I want to open a tea shop"
    })


