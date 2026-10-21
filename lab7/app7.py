
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Sales Dashboard")
st.write("Analyze sales by year, region, and product.")

# Create sample sales data
np.random.seed(42)

df = pd.DataFrame({
    "Year": np.random.choice([2022, 2023, 2024], 200),
    "Region": np.random.choice(
        ["North", "South", "East", "West"], 200
    ),
    "Product": np.random.choice(
        ["Laptop", "Phone", "Tablet"], 200
    ),
    "Sales": np.random.randint(1000, 10000, 200)
})

# Sidebar filters
st.sidebar.header("Filters")

years = st.sidebar.multiselect(
    "Select Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

regions = st.sidebar.multiselect(
    "Select Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

products = st.sidebar.multiselect(
    "Select Product",
    sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

# Filter the data
filtered_df = df[
    df["Year"].isin(years)
    & df["Region"].isin(regions)
    & df["Product"].isin(products)
]

# Display KPI metrics
st.subheader("Sales Overview")

col1, col2, col3 = st.columns(3)

total_sales = filtered_df["Sales"].sum()

average_sales = (
    filtered_df["Sales"].mean()
    if not filtered_df.empty
    else 0
)

total_records = len(filtered_df)

col1.metric("Total Sales", f"₹{total_sales:,}")
col2.metric("Average Sales", f"₹{average_sales:,.2f}")
col3.metric("Total Records", total_records)

# Bar chart: Sales by Region
st.subheader("Sales by Region")

if not filtered_df.empty:
    region_sales = filtered_df.groupby("Region")["Sales"].sum()
    st.bar_chart(region_sales)
else:
    st.info("No data available for the selected filters.")

# Line chart: Sales by Year
st.subheader("Sales by Year")

if not filtered_df.empty:
    yearly_sales = filtered_df.groupby("Year")["Sales"].sum()
    st.line_chart(yearly_sales)

# Display filtered data
st.subheader("Sales Data")
st.dataframe(filtered_df, use_container_width=True)

# Download filtered data
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered CSV",
    data=csv,
    file_name="sales_data.csv",
    mime="text/csv"
)
