from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents import linkedin_lookup_agent
from third_parties import scrape_linkedin_profile


def who_is(name: str):
    prompt = PromptTemplate(
        input_variables=["information"],
        template="""
            Given the following information: {information}
            
            Your goal is to write:
             1. a summary of the information.
             2. two key takeaways from the information.
             
             No need to describe the information in detail, just summarize it and write two key takeaways.
        """,
    )

    llm = ChatOpenAI(
        temperature=0.0,
        # max_tokens=150,
        model="gpt-3.5-turbo",
    )
    chain = LLMChain(llm=llm, prompt=prompt)

    linkedin_profile_url = linkedin_lookup_agent(
        person_name=name,
    )
    linkedin_profile = scrape_linkedin_profile(linkedin_profile_url)

    result = chain.run(information=linkedin_profile)

    print(result)
    with open("output.txt", "w") as file:
        file.write(result)


if __name__ == "__main__":
    user_input = input("Enter the name of the person with additional context:")
    who_is(user_input)
