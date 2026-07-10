import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Visualization",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Visualization Dashboard")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("output/cleaned_data.csv")

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

col1.metric("⭐ Average Rating", round(df["Rating"].mean(), 2))
col2.metric("📝 Total Reviews", len(df))
col3.metric("📦 Products", df["Product_name"].nunique())

st.divider()

# ======================================================
# Rating Distribution
# ======================================================

st.subheader("⭐ Rating Distribution")

rating_count = df["Rating"].value_counts().sort_index()

fig = px.bar(
    x=rating_count.index,
    y=rating_count.values,
    labels={"x":"Rating","y":"Number of Reviews"},
    text=rating_count.values,
    title="Rating Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================================
# Pie Chart
# ======================================================

st.subheader("🥧 Rating Percentage")

fig = px.pie(
    names=rating_count.index,
    values=rating_count.values,
    title="Rating Percentage"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================================
# Top 10 Products
# ======================================================

st.subheader("🏆 Top 10 Most Reviewed Products")

top_products = (
    df["Product_name"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_products.columns = ["Product", "Reviews"]

fig = px.bar(
    top_products,
    x="Reviews",
    y="Product",
    orientation="h",
    text="Reviews",
    title="Top Reviewed Products"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================================
# Review Length Distribution
# ======================================================

st.subheader("📏 Review Length Distribution")

df["Review Length"] = df["Review"].str.len()

fig = px.histogram(
    df,
    x="Review Length",
    nbins=30,
    title="Review Length Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ======================================================
# Rating Summary Table
# ======================================================

st.subheader("📋 Rating Summary")

summary = df.groupby("Rating").agg(
    Reviews=("Rating", "count")
).reset_index()

st.dataframe(summary, use_container_width=True)