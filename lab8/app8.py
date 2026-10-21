
import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import os

st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸"
)

st.title("🌸 Iris Flower Prediction")
st.write("Enter flower measurements to predict its species.")

# Train and save the model if it does not exist
if not os.path.exists("model.pkl"):
    iris = load_iris()
    X = iris.data
    y = iris.target

    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)

    joblib.dump(model, "model.pkl")

# Load the trained model
model = joblib.load("model.pkl")

classes = ["Setosa", "Versicolor", "Virginica"]

# Prediction form
with st.form("prediction_form"):
    st.subheader("Enter Flower Measurements")

    sl = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
    sw = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
    pl = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
    pw = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

    submit = st.form_submit_button("Predict Flower")

# Store prediction history
if "history" not in st.session_state:
    st.session_state.history = []

if submit:
    features = np.array([[sl, sw, pl, pw]])

    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]

    st.success(f"Predicted Species: {classes[prediction]}")

    confidence = max(probabilities) * 100
    st.metric("Prediction Confidence", f"{confidence:.1f}%")

    # Display class probabilities
    st.subheader("Class Probabilities")

    probability_df = pd.DataFrame({
        "Species": classes,
        "Probability": probabilities
    })

    st.bar_chart(
        probability_df.set_index("Species")
    )

    # Save prediction in history
    st.session_state.history.append({
        "Sepal Length": sl,
        "Sepal Width": sw,
        "Petal Length": pl,
        "Petal Width": pw,
        "Prediction": classes[prediction]
    })

# Display prediction history
st.subheader("Prediction History")

if st.session_state.history:
    st.dataframe(
        pd.DataFrame(st.session_state.history),
        use_container_width=True
    )

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("Your predictions will appear here.")
