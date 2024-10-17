from types_for_crew import BusinessIdeaAgent, BusinessIdeaTask
from crewai import Agent


# Agents
agents: dict[str, BusinessIdeaAgent] = {
    "breaking_down_info": {
        "role": "Senior Brand Manager",
        "goal": (
            "Analyze the provided refined business idea and analyze mission, vision, values and target audience of the business "
            "Identify the core product/service differentiator. meaning unique selling proposition "
            "Assess marketing positioning with respect to competators, industry trends and local trends "
            "List down all your findings in a structured manner for a branding company to take all this info and build a brand "
            "for the business idea."
        ),
        "backstory": (
            "You have proven experience in the industry for niche businesses as a branding company. "
            "You have a strong portfolio with successful brand transformations. you also provide strategic services like market research, brand positioning, and storytelling and understand all nook and crannies "
            "You also have a thorough understanding of full-service offerings including design, digital marketing, and campaign execution "
            "you provide businesses with clear, actionable insights into the branding that make their business successful "
            "your adaptability to evolving trends and client preferences is unmatched"
        ),
        "verbose": True,
        'allow_delegation': False
    },
}

# Tasks
tasks: dict[str, BusinessIdeaTask] = {
    
    "breaking_down_info": {
        "description": (
            "Using the provided {refined_business_idea} and {marketing_strategy}, "
            "analyze the core components of the business. Identify the unique selling proposition (USP) that differentiates it from competitors. "
            "Evaluate the marketing positioning based on competitors, industry_trends, and local_trends. "
            "Provide actionable insights into how these elements can be leveraged to create a strong, cohesive brand identity. "
            "suggest mission, vision, values and target audiance"
            "Document the findings in a structured format for the branding company to use."
        ),
        "expected_output": (
            "A structured document listing the core business components (mission, vision, values, target audience), "
            "the unique selling proposition, and an analysis of the market positioning, including competitor, industry, and local trends. "
            "This document will be prepared for use by the branding company."
        ),
        "agent": "Senior Brand Manager",
        "async_execution": False,
        "output_file": "branding_analysis_output.csv"
    },
}
