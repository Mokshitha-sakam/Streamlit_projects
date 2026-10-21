
import streamlit as st

st.set_page_config(
    page_title="Lab 5",
    page_icon="🧮"
)

st.title("Lab 5 - User Input and Widgets")
st.write("Explore Streamlit input widgets.")

name = st.text_input("Enter your name")

age = st.slider(
    "Select your age",
    min_value=1,
    max_value=100,
    value=18
)

city = st.selectbox(
    "Choose your city",
    ["Tirupati", "Chennai", "Hyderabad", "Bengaluru", "Other"]
)

hobbies = st.multiselect(
    "Select your hobbies",
    ["Reading", "Coding", "Music", "Sports", "Drawing"]
)

rating = st.radio(
    "How do you rate Streamlit?",
    ["Excellent", "Good", "Average"]
)

if st.button("Submit"):
    st.success("Details submitted successfully!")

    st.write("Name:", name if name else "Not provided")
    st.write("Age:", age)
    st.write("City:", city)
    st.write("Hobbies:", ", ".join(hobbies) if hobbies else "None selected")
    st.write("Rating:", rating)

if st.checkbox("Show a message"):
    st.info("You are learning Streamlit widgets!")
