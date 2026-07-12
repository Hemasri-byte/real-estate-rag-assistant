"""
loader.py

Loads all PDF documents from the knowledge base.
"""

from langchain_community.document_loaders import PyPDFDirectoryLoader


PDF_FOLDER = "data/pdf"


def load_documents():
    """
    Load all PDF documents from the data/pdf folder.
    """

    loader = PyPDFDirectoryLoader(PDF_FOLDER)

    documents = loader.load()

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print(f"Documents Loaded: {len(docs)}")