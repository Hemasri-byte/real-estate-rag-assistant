import os

from langchain_chroma import Chroma

from src.embeddings import get_embedding_model
from src.vectordb import create_vector_db


def get_retriever():

    if not os.path.exists("chroma_db"):

        print("Creating Vector Database...")

        create_vector_db()

    embedding_model = get_embedding_model()

    vector_db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model,
    )

    return vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )