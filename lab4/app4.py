
import streamlit as st

st.set_page_config(
    page_title="Lab 4",
    page_icon="📊",
    layout="centered"
)

st.title("Lab 4 - Streamlit Data Display")

st.header("Display Text")
st.write("Welcome to my Streamlit application!")

st.header("Display Data")
student_data = {
    "Name": ["Mokshitha", "Student 2", "Student 3"],
    "Course": ["B.Tech CSE", "B.Tech ECE", "BBA"],
    "Marks": [90, 85, 88]
}

st.write("Student Data Table")
st.dataframe(student_data)

st.header("Display a Static Table")
st.table(student_data)

st.header("Display JSON")
st.json(student_data)

st.header("Display Metrics")
col1, col2, col3 = st.columns(3)

col1.metric("Students", 3)
col2.metric("Average Marks", 87.7)
col3.metric("Highest Marks", 90)
