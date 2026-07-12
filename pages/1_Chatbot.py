import os
import streamlit as st

from src.chain import get_answer_and_sources

# ----------------------------------------------------
# LOGIN PROTECTION
# ----------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.error("❌ Please login first.")
    st.stop()

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="Real Estate AI Assistant",
    page_icon="🏠",
    layout="wide",
)

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

    st.write(
        """
This AI Assistant answers questions from a Real Estate
Knowledge Base using Retrieval-Augmented Generation (RAG).

### Technologies Used

- 🤖 Google Gemini 2.5 Flash
- 🦜 LangChain
- 🗂️ ChromaDB
- 📄 Retrieval-Augmented Generation (RAG)
- 🎨 Streamlit
"""
    )

    st.markdown("---")

    st.write("### 📂 Dataset")

    st.write("✔ Project Brochures")
    st.write("✔ Builder Profiles")
    st.write("✔ Pricing Documents")
    st.write("✔ Payment Plans")
    st.write("✔ RERA Documents")
    st.write("✔ FAQs")
    st.write("✔ Legal Documents")
    st.write("✔ Floor Plans")

    st.markdown("---")

    st.write("### 💡 Example Questions")

    st.markdown("#### 🏢 Skyline Horizon Towers")

    st.write("• What is the possession date of Skyline Horizon Towers?")
    st.write("• Who is the developer of Skyline Horizon Towers?")
    st.write("• What is the RERA number of Skyline Horizon Towers?")
    st.write("• What is the price range of Skyline Horizon Towers?")
    st.write("• What amenities are available in Skyline Horizon Towers?")

    st.markdown("---")

    st.markdown("#### 🏢 Horizon Business Park")

    st.write("• What is the possession date of Horizon Business Park?")
    st.write("• Who is the developer of Horizon Business Park?")
    st.write("• What is the RERA number of Horizon Business Park?")
    st.write("• What is the price range of Horizon Business Park?")
    st.write("• What amenities are available in Horizon Business Park?")

    st.markdown("---")

    if st.button("🗑 Clear Conversation"):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.messages = []
        st.switch_page("app.py")

    st.success("Logged out successfully.")

    st.switch_page("app.py")
# ----------------------------------------------------
# MAIN PAGE
# ----------------------------------------------------

st.title("🏠 Real Estate AI Assistant")

st.caption("Retrieval-Augmented Generation (RAG) using Google Gemini")

st.write(
    """
Welcome! 👋

Ask questions about the real estate projects available
in the knowledge base.
"""
)

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

    # --------------------------------------------
    # Store User Message
    # --------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # --------------------------------------------
    # Build Conversation History
    # --------------------------------------------

    history = ""

    for msg in st.session_state.messages:

        history += f"{msg['role']}: {msg['content']}\n"

    # --------------------------------------------
    # Generate AI Response
    # --------------------------------------------

    with st.spinner("Searching documents..."):

        answer, docs = get_answer_and_sources(
            question,
            history
        )

    # --------------------------------------------
    # Prepare Source List
    # --------------------------------------------

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

    # --------------------------------------------
    # Final Answer
    # --------------------------------------------

    final_answer = f"""
{answer}

---

### 📄 Sources

{source_text}
"""

    # --------------------------------------------
    # Store Assistant Message
    # --------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )

    # --------------------------------------------
    # Display Assistant Message
    # --------------------------------------------

    with st.chat_message("assistant"):

        st.markdown(final_answer)