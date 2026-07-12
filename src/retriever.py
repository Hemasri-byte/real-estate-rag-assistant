"""
retriever.py

Loads the Chroma Vector Database.
If it doesn't exist, it creates it automatically.
"""

import os

from langchain_chroma import Chroma

from src.embeddings import get_embedding_model
from src.vectordb import create_vector_db


def get_retriever():

    embedding_model = get_embedding_model()

    # If database doesn't exist, create it
    if not os.path.exists("chroma_db"):

        print("Creating Chroma Vector Database...")

        create_vector_db()

    vector_db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model,
    )

    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    docs = retriever.invoke("What is the RERA number?")

    print(f"Retrieved {len(docs)} documents.")