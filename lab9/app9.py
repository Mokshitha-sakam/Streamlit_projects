
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Lab 9 - Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My Chatbot")
st.write("Welcome! Ask me a simple question.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Display and save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Simple rule-based responses
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        response = "Hello! How can I help you?"
    elif "name" in text:
        response = "I am your Streamlit chatbot."
    elif "time" in text:
        response = "The current time is " + datetime.now().strftime("%I:%M %p")
    elif "how are you" in text:
        response = "I am doing great! How are you?"
    elif "bye" in text:
        response = "Goodbye! Have a nice day."
    else:
        response = "I am a simple chatbot. Try asking hello, my name, or the time."

    # Save bot response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()

# Clear conversation
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
