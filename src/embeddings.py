"""
embeddings.py

Creates and returns the Gemini Embedding Model.
"""

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def get_embedding_model():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:

        api_key = st.secrets["GOOGLE_API_KEY"]

    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=api_key,
    )

    return embedding_model


if __name__ == "__main__":

    embeddings = get_embedding_model()

    vector = embeddings.embed_query("What is RAG?")

    print("Embedding Model Loaded Successfully!")

    print(f"Vector Size: {len(vector)}")