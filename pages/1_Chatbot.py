import os
import streamlit as st

# ----------------------------------------------------
# PAGE CONFIG (MUST BE FIRST)
# ----------------------------------------------------

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide",
)

# ----------------------------------------------------
# LOGIN PROTECTION
# ----------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("❌ Please login first.")
    st.stop()

# ----------------------------------------------------
# SESSION STATE
# ----------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

with st.sidebar:

    st.title("🏠 Real Estate AI Assistant")

    st.markdown("---")

    st.write("### 🤖 About")

    st.write("""
This AI Assistant answers questions from a Real Estate Knowledge Base.

### Technologies

- 🤖 Google Gemini 2.5 Flash
- 🦜 LangChain
- 🗂️ ChromaDB
- 📚 Retrieval-Augmented Generation
- 🎨 Streamlit
""")

    st.markdown("---")

    st.write("### Example Questions")

    st.write("• What is the RERA number?")
    st.write("• Who is the developer?")
    st.write("• What is the possession date?")
    st.write("• What is the price?")
    st.write("• What amenities are available?")

    st.markdown("---")

    if st.button("🗑 Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.messages = []
        st.switch_page("app.py")

# ----------------------------------------------------
# MAIN PAGE
# ----------------------------------------------------

st.title("🏠 Real Estate AI Assistant")

st.caption("Retrieval-Augmented Generation (RAG) using Google Gemini")

st.write("Ask any question about the Real Estate documents.")

# ----------------------------------------------------
# DISPLAY CHAT HISTORY
# ----------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------------------------
# CHAT INPUT
# ----------------------------------------------------

question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    history = ""

    for msg in st.session_state.messages:
        history += f"{msg['role']}: {msg['content']}\n"

    # IMPORT ONLY WHEN NEEDED
    from src.chain import get_answer_and_sources

    with st.spinner("Searching documents..."):

        answer, docs = get_answer_and_sources(
            question,
            history
        )

    shown = set()
    sources = []

    for doc in docs:

        filename = os.path.basename(
            doc.metadata.get("source", "")
        )

        page = doc.metadata.get("page", 0) + 1

        key = (filename, page)

        if key not in shown:

            shown.add(key)

            sources.append(
                f"• **{filename}** (Page {page})"
            )

    source_text = "\n".join(sources)

    final_answer = f"""
{answer}

---

### 📄 Sources

{source_text}
"""

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(final_answer)