"""
vectordb.py

Creates and stores the Chroma Vector Database.
"""

from langchain_chroma import Chroma

from src.splitter import split_documents
from src.embeddings import get_embedding_model


def create_vector_db():

    chunks = split_documents()

    embedding_model = get_embedding_model()

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="chroma_db",
    )

    return vector_db


if __name__ == "__main__":

    db = create_vector_db()

    print("Vector Database Created Successfully!")

    print(f"Total Chunks: {db._collection.count()}")