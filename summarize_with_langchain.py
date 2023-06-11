from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

information = """
    Kendrick Lamar Duckworth (born June 17, 1987) is an American rapper and songwriter. Known for his progressive musical styles and socially conscious songwriting, he is often considered one of the most influential hip hop artists of his generation.[1][2] Born and raised in Compton, California, Lamar began his career as a teenager performing under the stage name K.Dot. He quickly garnered local attention which led to him signing a recording contract with Top Dawg Entertainment (TDE) in 2005.[3]
    
    After becoming a founding member of the hip hop supergroup Black Hippy, Lamar dropped his stage name and started using his first and middle names professionally. In 2011, he released his debut studio album Section.80, a conscious hip hop record. The album was met with positive reviews and included his debut single "HiiiiPower". In 2012, Lamar secured a record deal with Dr. Dre's Aftermath Entertainment, under the aegis of Interscope Records, and released his second studio album Good Kid, M.A.A.D City. The West Coast and gangsta rap influenced album garnered widespread critical recognition and commercial success, while including the singles "Swimming Pools (Drank)", "Backseat Freestyle", and "Bitch, Don't Kill My Vibe".[4]
    
    A visit to South Africa inspired Lamar's jazz-flavored third studio album To Pimp a Butterfly (2015).[5] It received universal acclaim and became his first number-one album on the Billboard 200.[6] The same year, he topped the Billboard Hot 100 for the first time with the remix of "Bad Blood" by Taylor Swift.[7] Lamar experimented with R&B, pop and psychedelic soul in his fourth studio album Damn (2017). It spawned his first solo number-one single "Humble" and became the first non-classical and non-jazz work to be awarded the Pulitzer Prize for Music.[8] Following a four-year hiatus, Lamar released his fifth studio album Mr. Morale & the Big Steppers (2022), which served as his swan song from TDE.[9] He has directed and produced several music videos and films with his creative partner Dave Free, with whom he founded the creative collective PGLang.
    
    Having sold over 70 million records in the United States alone, all of Lamar's studio albums have been certified platinum or higher by the Recording Industry Association of America (RIAA).[10] He has received numerous accolades throughout his career, including 17 Grammy Awards, a Primetime Emmy Award, two American Music Awards, six Billboard Music Awards, 11 MTV Video Music Awards, a Brit Award, and a nomination for an Academy Award. He was named MTV's Hottest MC in the Game in 2012.[11] In 2015, Lamar received the California State Senate's Generational Icon Award. He has been featured in listicles such as the Time 100 and Forbes 30 Under 30.[12][13] Three of his studio albums were included on Rolling Stone's 2020 ranking of the 500 Greatest Albums of All Time.
"""

prompt = PromptTemplate(
    input_variables=["information"],
    template="""
        Given the following information: {information}
        
        Your goal is to write:
         1. a summary of the information.
         2. two key takeaways from the information.
    """,
)

llm = ChatOpenAI(temperature=0.0, max_tokens=150, model="gpt-3.5-turbo")
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(information=information))
