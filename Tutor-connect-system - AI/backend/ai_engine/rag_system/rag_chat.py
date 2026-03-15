from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA


def ask_rag(question, vector_store):

    llm = ChatOpenAI(model="gpt-4o-mini")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    result = qa.run(question)

    return result