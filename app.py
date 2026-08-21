import streamlit as st

st.set_page_config(page_title="EFALL Hub", layout="wide")
st.title("🌟 EFALL: Educated Mother Education Nation")
st.write("Welcome to your centralized early years learning portal!")

if "lang" not in st.session_state:
    st.session_state.lang = "English"

col1, col2 = st.columns(2)
with col1:
    if st.button("English Portal", use_container_width=True):
        st.session_state.lang = "English"
with col2:
    if st.button("اردو پورٹل", use_container_width=True):
        st.session_state.lang = "Urdu"

st.info(f"Current Selected Language: **{st.session_state.lang}**")
topic = st.text_input("Enter Inquiry Topic:", "Ecosystems & Water Cycles")
if st.button("Generate Lesson Plan"):
    st.success(f"Generated plan for topic: {topic}!")
