# 🏠 Real Estate AI Assistant using RAG

An AI-powered Real Estate Question Answering Assistant built using **Google Gemini**, **LangChain**, **ChromaDB**, and **Streamlit**.

The application uses **Retrieval-Augmented Generation (RAG)** to answer questions from a Real Estate Knowledge Base containing brochures, builder profiles, RERA documents, pricing documents, payment plans, FAQs, and legal documents.

---

# Features

- 🔐 Login Authentication
- 🤖 Google Gemini 2.5 Flash LLM
- 📚 Retrieval-Augmented Generation (RAG)
- 🦜 LangChain Framework
- 🗂️ ChromaDB Vector Database
- 💬 Context-Aware Conversations
- 📄 Source References for Every Answer
- ⚡ Semantic Search using Embeddings
- 🎨 Interactive Streamlit User Interface

---

# Tech Stack

- Python 3.13
- Google Gemini 2.5 Flash
- LangChain
- ChromaDB
- Streamlit
- python-dotenv

---

# Project Structure

```
real_estate_rag/
│
├── app.py
├── pages/
│   └── 1_Chatbot.py
│
├── src/
│   ├── auth.py
│   ├── chain.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── prompts.py
│   ├── retriever.py
│   ├── splitter.py
│   ├── utils.py
│   └── vectordb.py
│
├── data/
│   ├── pdf/
│   ├── markdown/
│   ├── html/
│   └── docx/
│
├── chroma_db/
├── requirements.txt
├── README.md
└── .env
```

---

# Dataset

The knowledge base contains multiple real estate projects including:

- Skyline Horizon Towers
- Horizon Business Park
- Meridian Greens Residency
- Meridian Lakeview Villas
- UrbanNest Heights
- UrbanNest Residency

Documents include:

- Project Brochures
- Builder Profiles
- Pricing Documents
- Payment Plans
- RERA Documents
- FAQs
- Legal Documents
- Floor Plans

---

# Installation

Clone the repository

```bash
git clone https://github.com/Hemasri-byte/real-estate-rag-assistant.git
```

Move into the project

```bash
cd real-estate-rag-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Login Credentials

Username

```
Hema Sri
```

Password

```
Hema@123
```

---

# Example Questions

- What is the possession date of Skyline Horizon Towers?
- Who is the developer of Skyline Horizon Towers?
- What is the RERA number of Horizon Business Park?
- What amenities are available in Meridian Lakeview Villas?
- What is the price range of Skyline Horizon Towers?
- Which banks provide home loans?

---

# Sample Workflow

1. Login
2. Open Chatbot
3. Ask a Real Estate question
4. Retrieve relevant documents
5. Generate an answer using Gemini
6. Display source documents

---

# Technologies Used

- Google Gemini 2.5 Flash
- LangChain
- ChromaDB
- Streamlit
- Python

---

# Future Improvements

- Multi-user Authentication
- Admin Dashboard
- PDF Upload Support
- Conversation Export
- Voice Input
- Hybrid Search
- Cloud Database Integration

---

# Author

**Hemasri Takkella**

GitHub

https://github.com/Hemasri-byte

---

# License

This project is developed for educational purposes as part of a Generative AI assignment.