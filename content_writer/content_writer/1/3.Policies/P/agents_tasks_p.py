from types_for_crew import BusinessIdeaAgent, BusinessIdeaTask
from crewai import Agent


# Agents
agents: dict[str, BusinessIdeaAgent] = {
    "government_policy_extractor": {
        "role": "Government Policy Expert",
        "goal": (
            "Analyze the provided refined business idea, business name, and location to identify relevant government policies and regulations. "
            "Search for official documents, laws, and guidelines specific to the business and location. "
            "Extract key policies, regulations, and compliance requirements that pertain to the business idea. "
            "Present the findings in an organized manner, highlighting necessary compliance steps, permits, and legal considerations. "
            "Save the extracted policies and compliance information in a structured .csv file."
        ),
        "backstory": (
            "As an expert in government policies and regulations, you specialize in identifying and interpreting the legal framework "
            "that affects businesses in different jurisdictions. Your ability to navigate complex legal documents and extract relevant information "
            "ensures that businesses are well-informed about their regulatory obligations. With a deep understanding of legal language and regulatory systems, "
            "you provide businesses with clear, actionable insights into the policies that govern their operations, enabling them to comply effectively and avoid legal pitfalls."
        ),
        "verbose": True,
        'allow_delegation': False
    },
    "company_policy_strategist": {
        "role": "Expert Company Policy Strategist",
        "goal": (
            "Utilize the provided business idea, business name, location, and the government policy output to develop a comprehensive strategy. "
            "This strategy should outline how the business can comply with necessary regulations while minimizing restrictions and competitive threats. "
            "Devise a clear plan for the policy writer to draft policies that protect the company's interests, ensuring compliance without compromising competitiveness. "
            "Identify potential legal loopholes, compliance strategies, and internal policies that mitigate the impact of government regulations and deter competitive actions. "
            "Document the strategy in a structured format, providing a detailed outline and key points for the policy writer to expand upon."
        ),
        "backstory": (
            "As a seasoned policy strategist, your expertise lies in creating robust strategies that help businesses navigate complex legal environments and competitive landscapes. "
            "With a deep understanding of government regulations and corporate policy-making, you design strategies that not only ensure compliance but also protect the company’s interests. "
            "Your strategic insights enable businesses to operate within legal boundaries while maintaining a competitive edge. "
            "You are known for your ability to foresee potential challenges and develop proactive measures that safeguard the business from regulatory and competitive threats."
        ),
        "verbose": True,
        'allow_delegation': False
    },
    "company_policy_writer": {
        "role": "Professional Company Policy Writer",
        "goal": (
            "Utilize the strategic layout from the Company Policy Strategist and the relevant government policies to draft well-structured, comprehensive company policies. "
            "Ensure that the policies are practical, realistic, and risk-mitigating, fully compliant with all legal requirements, and designed to help the company thrive against competitors. "
            "Cover areas such as compliance, operational standards, employee conduct, data protection, and competitive strategy. "
            "Save the finalized policies in a structured document, ensuring clarity and ease of understanding for all stakeholders."
        ),
        "backstory": (
            "As a professional policy writer, your expertise lies in translating strategic guidelines and legal frameworks into detailed, actionable company policies. "
            "You have a keen eye for detail and a deep understanding of how to craft policies that not only comply with regulations but also support the company's growth and operational efficiency. "
            "Your writing is known for its clarity and precision, making complex legal and strategic requirements accessible and understandable. "
            "You excel at balancing regulatory compliance with business needs, creating policies that are robust, enforceable, and aligned with the company’s strategic goals."
        ),
        "verbose": True,
        'allow_delegation': False
    }
}

# Tasks
tasks: dict[str, BusinessIdeaTask] = {
    "policy_extraction": {
        "description": (
            "Using the provided {refined_business_idea}, {name}, and {location}, "
            "identify relevant government policies and regulations that affect the business. "
            "Search for official policy documents and legal guidelines from the specified country or state. "
            "Extract and summarize the key regulations, permits, licenses, and compliance requirements needed for the business to operate legally. "
            "Document the findings in a structured .csv file."
        ),
        "expected_output": (
            "A detailed .csv file listing all relevant government policies, compliance requirements, permits, and legal considerations "
            "related to the {refined_business_idea} in {location}."
        ),
        "agent": "government_policy_extractor",
        "async_execution": False,
        "output_file": "policy_extraction_output.csv"
    },
    "strategy_layout": {
        "description": (
            "Using the provided {refined_business_idea}, {name}, {location}, and government_policy_output, "
            "devise a strategic layout for developing comprehensive company policies. "
            "Identify key areas where the business needs protection from government regulations and competitive threats. "
            "should provide detailed guidelines and SOPs (Standard Operating Procedures) for critical operational areas. "
            "Outline strategies for compliance and risk mitigation, including exploiting legal advantages and reinforcing company defenses against competitors. "
            "Expand on Legal Advantages, include specific information on how to apply for tax incentives and avoid common pitfalls. "
            "should also address data breach response plan to strengthen data protection policies. "
            "Provide a clear, structured plan with key points for the policy writer agent to expand into detailed company policies. "
            "Include specific instences and examples where the strategy is teking"
        ),
        "expected_output": (
            "A detailed strategy document with key points outlining how the business can comply with government policies and protect itself from competitive threats. "
            "This document will serve as a foundation for the policy writer to draft specific company policies."
        ),
        "agent": "company_policy_strategist",
        "async_execution": False,
        "output_file": "strategy_layout_output.csv"
    },
    "company_policy_document": {
        "description": (
            "Using the provided {refined_business_idea}, strategic_layout_output from the Company Policy Strategist and government_policy_output, "
            "draft a comprehensive set of company policies. "
            "Ensure the policies are well-structured, covering key areas such as compliance, risk management, operational procedures, and competitive strategy. "
            "policies should exploit legal advantages including detailed steps on how to qualify for these incentives and potential pitfalls to avoid "
            "The policies should be practical and realistic, fully compliant with all legal requirements, and crafted to protect the company from legal and competitive threats. "
            "The document should be written in a clear, professional language and structured for easy reference by all stakeholders. "
            "should consider Use case studies or hypothetical scenarios to illustrate the application of employee conduct policies. "
            "document should contain specific instructions, training requirements, and quality control measures which would strengthen operational efficiency where ever can "
        ),
        "expected_output": (
            "A complete set of well-structured company policies saved in a document. "
            "The document should cover all necessary aspects, ensuring full compliance with government regulations and providing clear guidelines for company operations and conduct."
        ),
        "agent": "company_policy_writer",
        "async_execution": False,
        "output_file": "company_policy_document.docx"
    }

}
