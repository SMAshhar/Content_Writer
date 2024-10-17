from types_for_crew import BusinessIdeaAgent, BusinessIdeaTask
from crewai import Agent


# Agents
agents: dict[str, BusinessIdeaAgent] = {
    "slogan_generator": {
        "role": "Slogan Specialist",
        "goal": (
            "Take the provided broken_down_info, including the business's mission, vision, values, target audience, "
            "and unique selling proposition (USP). Analyze the information to generate three distinct, compelling slogans "
            "that are fully aligned with the core message and brand identity. "
            "Ensure that the slogans resonate with the target audience and reflect the brand's positioning in the market."
        ),
        "backstory": (
            "You are a highly creative branding professional with extensive experience crafting impactful slogans for niche businesses. "
            "You understand the importance of aligning slogans with the business's core values, mission, and market positioning. "
            "You have a proven track record of creating slogans that capture attention, communicate the brand's USP, "
            "and drive engagement among the target audience. Your expertise in understanding market trends and audience preferences "
            "allows you to deliver slogans that are both timeless and relevant."
        ),
        "verbose": True,
        'allow_delegation': False
    }
}



# Tasks
tasks: dict[str, BusinessIdeaTask] = {
    
   "slogan_generation": {
        "description": (
            "Using the provided {broken_down_info}, including the business’s mission, vision, values, target audience, "
            "and unique selling proposition (USP), analyze the information to generate three distinct and compelling slogans. "
            "Ensure the slogans are aligned with the brand’s identity, resonate with the target audience, and effectively communicate the USP. "
            "Each slogan should reflect the brand's positioning in the market and differentiate it from competitors."
        ),
        "expected_output": (
            "A three line document containing three slogans only that are fully aligned with the business’s core values, "
            "mission, vision, and unique selling proposition. The slogans should be designed to appeal to the target audience "
            "and enhance the brand's positioning in the market."
        ),
        "agent": "Slogan Generator",
        "async_execution": False,
        "output_file": "slogan_output.csv"
    }
}
