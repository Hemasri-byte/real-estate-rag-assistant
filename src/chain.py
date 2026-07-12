from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI

from src.retriever import get_retriever

load_dotenv()

retriever = get_retriever()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)


def format_docs(docs):

    return "\n\n".join(
        f"""
===============================
SOURCE : {doc.metadata.get("source")}
PAGE   : {doc.metadata.get("page")}

{doc.page_content}
"""
        for doc in docs
    )


prompt = ChatPromptTemplate.from_template(
"""
You are an intelligent Real Estate AI Assistant.

Use ONLY the information available in the provided context.

Instructions:

1. Use the previous conversation if the current question depends on it.

2. If the user asks a follow-up question like:
   - "Who is the developer?"
   - "What is the RERA number?"
   - "What is the possession date?"
   then infer the project from the previous conversation whenever possible.

3. If multiple projects match and the previous conversation does not identify one, ask the user to specify the project.

4. Never make up information.

5. If the answer is unavailable, reply exactly:

I couldn't find that information in the provided documents.

------------------------

Context:

{context}

------------------------

Question:

{question}

------------------------

Answer:
"""
)


def get_answer_and_sources(question, chat_history=""):

    full_question = question

    if chat_history.strip():

        full_question = f"""
Previous Conversation:

{chat_history}

Current Question:

{question}
"""

    docs = retriever.invoke(full_question)

    context = format_docs(docs)

    chain = (
        RunnableLambda(
            lambda _: {
                "context": context,
                "question": full_question,
            }
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    answer = chain.invoke({})

    return answer, docs