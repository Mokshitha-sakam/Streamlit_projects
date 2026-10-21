
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Lab 6",
    page_icon="📊"
)

st.title("Lab 6 - File Upload and Pandas")
st.write("Upload a CSV file and analyze the data.")

file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Data Preview")
    st.dataframe(df)

    st.subheader("Statistics")
    st.write(df.describe())

    st.subheader("Filter Data")

    column = st.selectbox("Choose a column", df.columns)
    value = st.text_input("Enter a value to search")

    if value:
        filtered = df[
            df[column].astype(str).str.contains(value, case=False)
        ]
        st.dataframe(filtered)

    st.subheader("Sort Data")

    sort_column = st.selectbox(
        "Choose a column to sort",
        df.columns,
        key="sort_column"
    )

    st.dataframe(df.sort_values(sort_column))
