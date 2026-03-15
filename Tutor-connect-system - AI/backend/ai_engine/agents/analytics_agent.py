from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent


def create_agent():

    db = SQLDatabase.from_uri("postgresql://postgres:password@localhost:5432/tutorconnect")

    llm = ChatOpenAI(model="gpt-4o-mini")

    agent = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True
    )

    return agent