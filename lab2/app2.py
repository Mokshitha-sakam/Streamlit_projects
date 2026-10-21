
import streamlit as st
from datetime import date

st.set_page_config(page_title="Widgets Playground", layout="wide")

st.title("Widgets Playground")
st.write("Explore different Streamlit widgets!")

st.divider()

# Text input
name = st.text_input("Name")

# Number input
age = st.number_input("Age", min_value=1, max_value=100, value=20)

# Slider
marks = st.slider("Marks", min_value=0, max_value=100, value=75)

# Select box
city = st.selectbox("City", ["Chennai", "Mumbai", "Delhi"])

# Multiselect
skills = st.multiselect(
    "Skills",
    ["Python", "ML", "SQL", "Streamlit"]
)

# Radio button
gender = st.radio("Gender", ["Male", "Female", "Other"])

# Checkbox
agree = st.checkbox("I agree to terms")

# Date input
dob = st.date_input("Date of Birth", date(2000, 1, 1))

# File uploader
uploaded_file = st.file_uploader("Upload a file")

st.divider()

# Submit button
if st.button("Submit"):
    st.subheader("Your Details")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Marks:", marks)
    st.write("City:", city)
    st.write("Skills:", skills)
    st.write("Gender:", gender)
    st.write("Agreed to terms:", agree)
    st.write("Date of Birth:", dob)

    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
    else:
        st.info("No file uploaded.")

    if agree:
        st.success("Form submitted successfully!")
    else:
        st.warning("Please agree to the terms.")
