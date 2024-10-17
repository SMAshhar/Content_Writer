from types_for_crew import BusinessIdeaAgent, BusinessIdeaTask
from crewai import Agent

# Agents
agents: dict[str, BusinessIdeaAgent] = {
    "planner":{
        "role":"Experienced Business Planner",
        "goal":("Make sure to do amazing analysis on the given {name} and {plan} "
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
        "role":"Business White Paper Writer",
        "goal":("take in the data from planner agent and develop "
            "a fully detailed, complete and practical business plan "
            "with respect to the location, the budget and the name "
            "the brief should contain mission, vision, values and target audience of the business"
            "then brief it down to 8 - 10 lines and store in .md format"
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
}

# Tasks
tasks:dict[str, BusinessIdeaTask] = {
    "planning": {
        "description":(
            "Go through the provided {name} and {plan}. Go through each item and analyze it thoroughly "
            "use your high experience in businees planning, asses the business idea and generate "
            "a plan to build a more complete, realistic and robust business idea "
            "if the {plan} is unrealistic, remove the unrealistic part, give reason in paranthesis "
            "and replace with a better plan"
        ),
        "expected_output":(
            "after a thorough analysis of the business idea, budget, location from the given {plan} "
            "a list of pointers for improved business plan with a solid base for the writer agent to  "
            "build a realistic and practical business idea"
        ),
        "agent":Agent,
        "async_execution":False,
        'output_file':None
        },
    "writing":{
        "description":(
            "take in the planning task and generate a well verced and complete business idea "
            "including mission, vision, values and target audience of the business"
            "brief the idea down to 8-10 lines and save them in markdown format "
        ),
        "expected_output":(
            "a paragraph with the refined business idea"
        ),
        "agent":Agent,
        "async_execution":False,
        "output_file":"refined_business_idea.md"
    }
}