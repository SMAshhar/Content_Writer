from types_for_crew import BusinessIdeaAgent, BusinessIdeaTask
from crewai import Agent


# Agents
agents: dict[str, BusinessIdeaAgent] = {
    "market_researcher":{
        "role":"Experienced Marketing Researcher",
        "goal":("Leverage {refined_business_idea} and {budgeting} to conduct comprehensive research on the culture and market dynamics of {location}. " 
                "Identify key marketing needs and develop a tailored marketing strategy for the {refined_business_idea}. Break down these needs into "
                "actionable criteria, document them as bullet points, and save the results in a structured .csv file for easy reference. "
        ),
        # "tools" : [],
        "verbose":True,
        "backstory":(
            "As an expert marketing researcher, you have an impressive track record of turning business ideas "
            "into successful marketing strategies. With years of experience, you excel at diving deep into a given "
            "business concept, understanding its core essence, and tailoring strategies to fit the unique cultural "
            "and market dynamics of various locations. Your keen analytical skills enable you to identify market "
            "needs and break down complex requirements into actionable insights. You are known for your ability "
            "to distill information into concise, practical points, which makes you a trusted resource for "
            "developing data-driven marketing plans. Your expertise helps businesses navigate through market "
            "challenges and seize growth opportunities effectively."
        ),
        'allow_delegation':False
        # "llm":llm
    },
    "marketing_planner": {
        "role": "Strategic Marketing Planner",
        "goal": (
            "Use the Market Researcher's output, {refined_business_idea}, and {budgeting} to "
            "develop a detailed plan for how the marketing strategy will be formulated. "
            "Identify key components, methodologies, and resources required for crafting a comprehensive marketing strategy. "
            "Ensure the plan aligns with the cultural context, social norms, and biases of the target market. "
            "Document the structure and approach for the upcoming strategy creation process, providing clear guidelines "
            "and checkpoints for the agent responsible for drafting the strategy."
        ),
        "backstory": (
            "As a strategic marketing planner, you specialize in designing the blueprint for marketing strategy development. "
            "Your expertise lies in assessing research outputs and business goals to formulate a clear path for creating effective marketing strategies. "
            "With a deep understanding of marketing frameworks and strategic planning, you outline the process, structure, and critical elements required for "
            "a well-crafted strategy. You ensure that the strategy creation process is well-organized, culturally informed, and aligned with the business objectives."
        ),
        "verbose": True,
        'allow_delegation': False
    },
    "marketing_strategy_developer": {
        "role": "Proficient Marketing Strategy Developer",
        "goal": (
            "Utilize the Market Researcher's output and the Marketing Planner's outline to craft a comprehensive marketing strategy. "
            "Carefully review the inputs provided to understand the market context and strategic planning structure. "
            "Develop a detailed strategy by assembling effective, feasible, and proven content that aligns with the business goals and market needs. "
            "Ensure that the strategy is comprehensive, actionable, and well-documented. Save the completed marketing strategy in a .csv file for easy reference and implementation."
        ),
        "backstory": (
            "As a proficient marketing strategy developer, your strength lies in transforming research data and strategic plans into comprehensive marketing strategies. "
            "You possess a keen ability to synthesize complex information into clear, actionable strategies that drive business growth. "
            "With a focus on feasibility and effectiveness, you craft strategies that are both innovative and grounded in proven methodologies. "
            "Your attention to detail ensures that each aspect of the strategy is meticulously developed and tailored to the specific needs of the business and its target market."
        ),
        "verbose": True,
        'allow_delegation': False
    }

}

# Tasks
tasks: dict[str, BusinessIdeaTask] = {
    "market_research": {
        "description": (
            "Analyze the {refined_business_idea} and {budgeting}. "
            "Research the cultural and market dynamics of {location}, and identify key marketing needs specific to the business idea. "
            "Break down these needs into actionable points and develop a structured marketing strategy. "
            "Document all findings and insights in a .csv file."
        ),
        "expected_output": (
            "A structured .csv file containing identified marketing needs, strategy recommendations, and a detailed breakdown of market insights "
            "specific to {refined_business_idea} in {location}."
        ),
        "agent": "market_researcher",
        "async_execution": False,
    },
    "marketing_planning": {
        "description": (
            "Use the output from the 'market_research' task, along with {refined_business_idea} and {budgeting}, "
            "to create a detailed plan for formulating the marketing strategy. "
            "Identify key components, methodologies, and resources needed. Outline the structure and approach, ensuring it aligns with the "
            "cultural context, social norms, and biases of the market. "
            "Document the plan in a clear and structured format, providing guidelines and checkpoints for the next stage."
        ),
        "expected_output": (
            "A comprehensive planning document in a .csv file that outlines the steps, resources, and methodologies required to develop the marketing strategy. "
            "The document should serve as a blueprint for creating an effective marketing strategy."
        ),
        "agent": "marketing_planner",
        "async_execution": False,
    },
    "strategy_development": {
        "description": (
            "Leverage the outputs from 'market_research' and 'marketing_planning' tasks to develop a complete marketing strategy for {refined_business_idea}. "
            "Assemble the structure with effective, feasible, and proven content. "
            "Ensure the strategy addresses the identified market needs, follows the outlined plan, and is tailored to the business and market context. "
            "Save the final strategy in a .csv file."
        ),
        "expected_output": (
            "A comprehensive marketing strategy document saved in a .csv file, detailing actionable steps, strategies, and tactics to effectively market {refined_business_idea}. "
            "The strategy should be well-structured and ready for implementation."
        ),
        "agent": "marketing_strategy_developer",
        "async_execution": False,
    }
}
