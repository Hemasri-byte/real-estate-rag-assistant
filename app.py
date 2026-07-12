import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Session State
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# Already Logged In
# -----------------------------

if st.session_state.logged_in:

    st.success("✅ Login Successful!")

    st.info("Open the Chatbot page from the left sidebar.")

    if st.button("Logout"):

        st.session_state.logged_in = False

        st.rerun()

    st.stop()

# -----------------------------
# Login Screen
# -----------------------------

st.title("🏠 Real Estate AI Assistant")

st.subheader("Login")

username = st.text_input("Username")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "Hema Sri" and password == "Hema@123":

        st.session_state.logged_in = True

        st.success("Login Successful!")

        st.rerun()

    else:

        st.error("Invalid Username or Password")