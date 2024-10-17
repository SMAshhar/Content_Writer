from types_for_crew import BusinessIdeaAgent, BusinessIdeaTask
from crewai import Agent


# Agents
agents: dict[str, BusinessIdeaAgent] = {
    "business_researcher":{
        "role":"Experienced Business Researcher",
        "goal":("Use {refined_business_idea} to research on marketing benchmarks, tools, "
                "equipments, resources, licenses etc and list down all business needs "
                "and develop a detailed list of requirments for the start and continuous "
                "operation of the business and finally return the list in .csv format "
        ),
        # "tools" : [],
        "verbose":True,
        "backstory":(
            "as an expert business researcher, your prowess in "
            "studying the business idea provided to you "
            "understanding the needs of the business and develop an awesome "
            "breakdown the requirments into managable items is unmatched."
            "Your skills help pinpoint the necessary "
            "things that are required by the business "
        ),
        'allow_delegation':False
        # "llm":llm
    },
    "budget_assigner":{
        "role":"Experienced Senior Budget Manager",
        "goal":("take in the data from researcher agent "
            "use the tools available to you to get accurate information as per listed by the data provided "
            "verify the BOQ for being accurate in its findings  "
            "if things are not that accurate, replace them with accurate values "
            ),
        # "tools" : [search_tool, scrapping_tool],
        "verbose":True,
        "backstory":(
            "your experience in budgetting massive and small businesses is immeasurable "
            "now at the senior most position, you verify the budget provided by the business researcher "
            "use the tools provided to you to find accurate values and verify the data budget and BOQ "
            "given to you and set the accurate values for it as you find best "
        ),
        'allow_delegation':False
        # "llm":llm
    },
}

# Tasks
tasks:dict[str, BusinessIdeaTask] = {
    "business_requirements": {
        "description":(
            "Go through the provided {refined_business_idea} identify and list down business requirements "
            "list down all the requirements leaving nothing out including but not limitting to "
            "marketing benchmark, tools, equipment, resources, rents, licenses etc leave nothing out "
            "list down the requirements for the business idea to make the business succeed in a .md format "
        ),
        "expected_output":(
            "a thorough list on each and every requirement for the business idea {refined_business_idea} "
            "which leaves nothing out in a .md format"
        ),
        "agent":Agent,
        "async_execution":False,
        'output_file':None
        },
    "budget_assignment":{
        "description":(
            "develop a thorough budgetting on the provided list of requiremnts "
            "assign budget to each item. strive for more accurate prices as per the {location} "
            "write everything down in a .md file "
        ),
        "expected_output":(
            "a thorough list of each and every requirment with required budget for the {refined_business_idea} "
            "saved in a .md file "
        ),
        "agent":Agent,
        "async_execution":False,
        "output_file":"budgetting.md"
    }
}