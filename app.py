import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="centered"
)

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------------------------------------------
# IF ALREADY LOGGED IN
# ----------------------------------------------------

if st.session_state.logged_in:

    st.success("✅ Login Successful!")

    st.markdown("# 🏠 Real Estate AI Assistant")

    st.info(
        """
Welcome to the AI-powered Real Estate Assistant.

This application uses **Google Gemini**, **LangChain**, and **ChromaDB**
to answer questions from a Real Estate Knowledge Base using
**Retrieval-Augmented Generation (RAG)**.

👉 Click **🚀 Open Chatbot** below to start asking questions.
"""
    )

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
- 🔐 Secure Login
- 🤖 Google Gemini 2.5 Flash
- 🦜 LangChain
- 🗂️ ChromaDB
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Context-Aware Conversation
- 📄 Source References
- ⚡ Semantic Search
""")

    st.markdown("---")

    if st.button("🚀 Open Chatbot"):

        st.switch_page("pages/1_Chatbot.py")

    st.markdown("---")

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False
        st.rerun()

    st.stop()

# ----------------------------------------------------
# LOGIN SCREEN
# ----------------------------------------------------

st.title("🏠 Real Estate AI Assistant")

st.subheader("🔐 Login")

st.write("Please login to continue.")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "Hema Sri" and password == "Hema@123":

        st.session_state.logged_in = True

        st.success("✅ Login Successful!")

        st.rerun()

    else:

        st.error("❌ Invalid Username or Password")