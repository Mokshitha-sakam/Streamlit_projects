
import streamlit as st
import sqlite3
import hashlib

st.set_page_config(
    page_title="Lab 13 - Login and Signup",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 User Login and Signup")
st.write("Lab 13: User Authentication")

# Create database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")
conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


option = st.radio("Choose an option", ["Sign Up", "Login"])

if option == "Sign Up":
    st.subheader("Create an Account")

    username = st.text_input("Choose Username", key="signup_user")
    password = st.text_input(
        "Choose Password",
        type="password",
        key="signup_pass"
    )

    if st.button("Sign Up"):
        if username.strip() and password:
            try:
                cursor.execute(
                    "INSERT INTO users VALUES (?, ?)",
                    (username.strip(), hash_password(password))
                )
                conn.commit()
                st.success("Account created successfully! Please log in.")

            except sqlite3.IntegrityError:
                st.error("Username already exists. Choose another username.")
        else:
            st.warning("Please enter both username and password.")

else:
    st.subheader("Login to Your Account")

    username = st.text_input("Username", key="login_user")
    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )

    if st.button("Login"):
        cursor.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username.strip(), hash_password(password))
        )

        user = cursor.fetchone()

        if user:
            st.success(f"Welcome, {username}!")
            st.balloons()
        else:
            st.error("Invalid username or password.")

conn.close()
