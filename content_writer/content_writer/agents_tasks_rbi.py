from types_for_crew import ContentAgent, ContentTask

# Agents
agents: dict[str, ContentAgent] = {
    "searcher": {
        "role": "Experienced Internet Researcher",
        "goal": (
            "Search the web for reliable and relevant information on the given topic. "
            "Identify the most important facts, data, and perspectives that should be "
            "included in the article."
        ),
        "tools": [],  # Define the tools used for searching the web
        "verbose": True,
        "backstory": (
            "As an expert researcher, you have the ability to sift through large amounts "
            "of information and find the most relevant and credible sources. Your role is to "
            "provide the necessary data and insights to guide the planning and writing of the article."
        ),
        "allow_delegation": False
    },
    "planner": {
        "role": "Content Strategist",
        "goal": (
            "Plan the structure and flow of the article. Break down the information gathered "
            "by the searcher agent and organize it into a clear, logical outline. Ensure the content "
            "covers all necessary aspects and adheres to the intended goals."
        ),
        "tools": [],  # Define tools for content planning if applicable
        "verbose": True,
        "backstory": (
            "As an expert in content strategy, you can take raw information and create a compelling "
            "and structured narrative. Your job is to make sure the article's key points are clear, "
            "well-organized, and engaging for the reader."
        ),
        "allow_delegation": False
    },
    "writer": {
        "role": "Content Writer",
        "goal": (
            "Use the research and plan provided to write a complete and well-structured article. "
            "Ensure the content is engaging, clear, and aligns with the topic and strategy outlined "
            "by the planner. Save the final article in the specified format."
        ),
        "tools": [],  # Define any specific writing tools if applicable
        "verbose": True,
        "backstory": (
            "With years of experience in writing articles on various topics, you know how to translate "
            "a well-researched plan into a readable, engaging piece. Your task is to craft content that "
            "delivers value to the reader while adhering to the goals of the overall strategy."
        ),
        "allow_delegation": False
    }
}
# Tasks
tasks: dict[str, ContentTask] = {
    "searching": {
        "description": (
            "Search for credible and reliable sources related to the given {topic}. Gather important "
            "information that will help in the creation of a well-informed article."
        ),
        "expected_output": (
            "A comprehensive list of key insights, data points, and quotes gathered from reputable "
            "sources relevant to the {topic}."
        ),
        "agent": agents["searcher"],  # Assign the 'searcher' agent
        "async_execution": False,
        "output_file": None
    },
    "planning": {
        "description": (
            "Using the gathered information, create a structured plan or outline for the article. "
            "Ensure all the key points are logically arranged and that the article covers the "
            "required scope effectively."
        ),
        "expected_output": (
            "A detailed plan with a clear outline of sections, key points, and flow for the article."
        ),
        "agent": agents["planner"],  # Assign the 'planner' agent
        "async_execution": False,
        "output_file": None
    },
    "writing": {
        "description": (
            "Take the structured plan and research and develop a complete article that meets the "
            "objectives. Ensure clarity, engagement, and adherence to the topic."
        ),
        "expected_output": (
            "A fully written article based on the given plan, saved in a markdown format."
        ),
        "agent": agents["writer"],  # Assign the 'writer' agent
        "async_execution": False,
        "output_file": "./docs/final_article.md"
    }
}
