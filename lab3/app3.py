
import streamlit as st

st.set_page_config(
    page_title="Lab 3",
    page_icon="📘",
    layout="centered"
)

st.title("Lab 3 - Streamlit Widgets")
st.header("User Information")

name = st.text_input("Enter your name")
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)

course = st.selectbox(
    "Choose your course",
    ["B.Tech CSE", "B.Tech ECE", "BBA", "Other"]
)

skills = st.multiselect(
    "Select your skills",
    ["Python", "HTML", "CSS", "JavaScript", "SQL"]
)

if st.button("Submit"):
    st.success("Information submitted successfully!")
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Course:", course)
    st.write("Skills:", ", ".join(skills) if skills else "None selected")
