
import streamlit as st

# Page configuration - must be first
st.set_page_config(
    page_title="Hello App",
    page_icon="H",
    layout="wide"
)

# Headings and text
st.title("Hello Streamlit")
st.header("My First App")
st.subheader("Learning Basics")

st.write("Streamlit converts Python scripts into web apps.")
st.markdown("**Bold text**, *italic text*, and `code`.")

# Messages
st.success("App loaded successfully!")
st.info("This is an info message.")
st.warning("This is a warning.")
st.error("This is an error.")

# User inputs
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=1, max_value=100)

# Sample table
st.write("### Sample Data")
st.table({
    "Name": ["A", "B"],
    "Marks": [85, 90]
})

# Exercise 2: Display a Python code example
st.divider()
st.subheader("Python Code Example")

st.code("""
def greet(name):
    return f"Hello, {name}!"
""", language="python")
