from types_for_crew import ContentAgent, ContentTask

# Agents
agents: dict[str, ContentAgent] = {
    #  USE THE FOLLOWING WHEN TOOLS LIKE SEARCH TOOL AND SCRAP TOOLS ARE AVAILABLE. I.E. USING OPENAI
    # "searcher": {
    #     "role": "Experienced Internet Researcher",
    #     "goal": (
    #         "Search the web for reliable and relevant information on the given topic. "
    #         "Identify the most important facts, data, and perspectives that should be "
    #         "included in the article."
    #     ),
    #     "tools": [],  # Define the tools used for searching the web
    #     "verbose": True,
    #     "backstory": (
    #         "As an expert researcher, you have the ability to sift through large amounts "
    #         "of information and find the most relevant and credible sources. Your role is to "
    #         "provide the necessary data and insights to guide the planning and writing of the article."
    #     ),
    #     "allow_delegation": False
    # },
    "idea_maker": {
        "goal": (
            "Assemble detailed, reliable, and relevant information on the given {topic}. "
            "Identify the most important facts, data, and perspectives that should be included in the article. "
            "Your goal is to make sure the article is not only informative but also accurate, engaging, and "
            "structured in a way that is easy for the reader to follow."
        ),
        "tools": [],  # Define any tools like web search APIs or databases here
        "verbose": True,
        "backstory": (
            "As an expert content creator with years of experience in writing and editing, you have a knack "
            "for finding the most credible sources of information. You excel at filtering through large volumes "
            "of data to find what truly matters, ensuring that the final content is well-rounded, comprehensive, "
            "and devoid of filler. Your work involves making sure the article is factually accurate and provides "
            "value to the reader by offering fresh insights or a unique perspective on the topic."
        ),
        "allow_delegation": False,
    },
    "planner": {
                "role": "Content Strategist",
        "goal": (
            "Plan the structure and flow of the article. Break down the information gathered by the searcher agent "
            "and organize it into a clear, logical outline. Ensure the content covers all necessary aspects and adheres "
            "to the intended goals. Focus on the readability and coherence of the article while ensuring that it aligns with "
            "the target audience and desired tone."
        ),
        "tools": [],  # Define tools for content planning if applicable, such as mind-mapping tools or frameworks
        "verbose": True,
        "backstory": (
            "As an expert in content strategy, you excel at transforming raw data and information into a compelling narrative. "
            "Your strength lies in organizing key points and creating a logical, engaging flow that makes the article easy to follow "
            "for readers. You understand how to balance detailed content with a reader-friendly structure, ensuring that the article "
            "is informative yet engaging. Your expertise in content planning ensures that every part of the article serves a purpose "
            "and contributes to the overall goal of the piece."
        ),
        "allow_delegation": False  
    },
    "writer": {
        "role": "Content Writer",
        "goal": (
            "Use the research and plan provided to write a complete and well-structured article. "
            "Ensure the content is engaging, clear, and aligns with the topic and strategy outlined by the planner. "
            "Maintain consistency in tone, voice, and readability throughout the article. "
            "Save the final article in the specified format (e.g., markdown or text)."
        ),
        "tools": [],  # Define any specific writing tools if applicable, such as grammar checkers or style guides
        "verbose": True,
        "backstory": (
            "With years of experience in writing articles across various topics, you have mastered the art of translating "
            "detailed research and outlines into compelling and well-organized written content. "
            "Your expertise lies in crafting articles that are informative, clear, and engaging, delivering value to readers while "
            "maintaining the goals set by the content strategist. Whether it’s technical writing, blogs, or narratives, your writing "
            "style is adaptable, making you versatile in handling a wide range of topics."
        ),
        "allow_delegation": False  
    }
}
# Tasks
tasks: dict[str, ContentTask] = {
    "searching": {
        "description": (
            "Search for credible and reliable sources related to the given {topic}. "
            "Gather important information that will contribute to creating a well-informed article. "
            "This includes finding facts, statistics, opinions, and insights from authoritative websites, publications, and research papers. "
            "The search must ensure that the sources are trustworthy, relevant, and up-to-date."
        ),
        "expected_output": (
            "A comprehensive list of key insights, data points, statistics, and quotes, each annotated with its source. "
            "These insights will be highly relevant to the {topic} and useful for the next steps in the content creation process. "
            "The information should be synthesized in a concise yet complete manner, providing a foundation for the article."
        ),
        "agent": agents["idea_maker"],  # Assign the 'idea_maker' agent for the search task
        "async_execution": False,  # This task will execute synchronously to ensure accuracy and relevance
        "output_file": None  # Output is in memory; passed to the next task in the pipeline
    },
    
    "planning": {
        "description": (
            "Using the information gathered from the search task, create a structured outline for the article. "
            "This involves breaking down the key points, organizing them logically into sections, and ensuring "
            "that all important aspects of the {topic} are covered. "
            "Each section should have a clear purpose and be aligned with the article's goal, ensuring the flow is easy to follow. "
            "Ensure that the plan is comprehensive, covering the topic’s breadth while focusing on its most important aspects."
        ),
        "expected_output": (
            "A well-organized and structured article outline, including an introduction, body sections, and a conclusion. "
            "Each section will have a list of key points to be covered, with a logical flow ensuring that the article is coherent and comprehensive. "
            "This plan will serve as the blueprint for the article writing stage."
        ),
        "agent": agents["planner"],  # Assign the 'planner' agent for the content strategy task
        "async_execution": False,  # This task will be executed synchronously
        "output_file": None  # Output is passed to the next task
    },
    
    "writing": {
        "description": (
            "Using the structured plan and research provided, develop a complete, well-written article. "
            "The writing should ensure clarity and engagement, following the structure laid out by the planner. "
            "Each section should be developed thoroughly, with smooth transitions between sections. "
            "The tone should match the target audience, and the content should align with the overall goals of the article. "
            "Make sure the article is free of grammatical errors, factually accurate, and adheres to the given {topic}."
        ),
        "expected_output": (
            "A polished and fully developed article based on the plan and research provided. "
            "The final product should be engaging, clear, and concise, ensuring that the key points are communicated effectively. "
            "The article will be saved in markdown format, with appropriate headings, subheadings, and formatting for readability."
        ),
        "agent": agents["writer"],  # Assign the 'writer' agent for the final writing task
        "async_execution": False,  # The article will be written synchronously to ensure accuracy
        "output_file": "./docs/final_article.md"  # The final article will be saved to this file path
    }
}