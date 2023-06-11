from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, AgentType, Tool

from tools.tools import get_linkedin_profile_url


def lookup(person_name):
    """
    Lookup a person's profile URL on LinkedIn.
    """

    llm = ChatOpenAI(temperature=0.0, max_tokens=150, model_name="gpt-3.5-turbo")
    prompt = PromptTemplate(
        input_variables=["person_name"],
        template="""
            You are an AI assistant that's optimized to lookup people's profiles on LinkedIn.
            
            Given a person's name {person_name}, you should return their LinkedIn profile URL.
            
            Your answer should be a URL.
        """,
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile",
            description="useful for finding LinkedIn profiles by the name of a person",
            func=get_linkedin_profile_url,
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    linkedin_profile_url = agent.run(prompt.format(person_name=person_name))

    return linkedin_profile_url
