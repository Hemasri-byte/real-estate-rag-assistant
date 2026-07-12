"""
retriever.py

Loads the Chroma Vector Database and creates a Retriever.
"""

from langchain_chroma import Chroma

from src.embeddings import get_embedding_model


def get_retriever():

    # Load the embedding model
    embedding_model = get_embedding_model()

    # Load the existing Chroma Vector Database
    vector_db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model,
    )

    # Create Retriever
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={
            "k": 3
        }
    )

    return retriever


if __name__ == "__main__":

    retriever = get_retriever()

    query = "What is the RERA number?"

    docs = retriever.invoke(query)

    print(f"Retrieved {len(docs)} documents.\n")

    for i, doc in enumerate(docs, start=1):

        print("=" * 60)
        print(f"Result {i}")
        print("=" * 60)

        print("Source :", doc.metadata.get("source"))
        print("Page   :", doc.metadata.get("page"))

        print("\nContent:\n")
        print(doc.page_content[:500])

        print("\n")