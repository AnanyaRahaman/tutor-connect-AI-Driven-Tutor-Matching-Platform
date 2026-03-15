from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from embeddings import get_embeddings


def build_vector_store(tutors):

    docs = []

    for tutor in tutors:

        text = f"""
        Tutor: {tutor['name']}
        Subject: {tutor['subject']}
        Rating: {tutor['rating']}
        Price: {tutor['price']}
        Experience: {tutor['experience']}
        """

        docs.append(Document(page_content=text))

    embeddings = get_embeddings()

    db = FAISS.from_documents(docs, embeddings)

    return db