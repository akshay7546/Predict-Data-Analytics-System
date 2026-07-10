import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Dataset",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Dataset Overview")

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("output/cleaned_data.csv")

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("📄 Rows", df.shape[0])
col2.metric("📊 Columns", df.shape[1])
col3.metric("❌ Missing Values", int(df.isnull().sum().sum()))
col4.metric("🔁 Duplicate Rows", int(df.duplicated().sum()))

st.divider()

# ==========================================================
# Dataset Preview with Search, Filter & Download
# ==========================================================

st.subheader("📋 Dataset Preview")

# Search Product
search = st.text_input(
    "🔍 Search Product",
    placeholder="Type product name..."
)

# Rating Filter
ratings = sorted(df["Rating"].unique())

selected_ratings = st.multiselect(
    "⭐ Filter by Rating",
    options=ratings,
    default=ratings
)

# Filter Dataset
filtered_df = df[df["Rating"].isin(selected_ratings)]

if search:
    filtered_df = filtered_df[
        filtered_df["Product_name"].str.contains(
            search,
            case=False,
            na=False
        )
    ]

# Download Button
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

# Show Total Records
st.success(f"Showing {len(filtered_df)} records")

# Interactive Table
st.dataframe(
    filtered_df,
    use_container_width=True,
    height=450
)

st.divider()

# ==========================================================
# Filter Summary
# ==========================================================

st.subheader("📈 Filter Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Filtered Rows",
    len(filtered_df)
)

col2.metric(
    "Average Rating",
    round(filtered_df["Rating"].mean(), 2)
)

col3.metric(
    "Unique Products",
    filtered_df["Product_name"].nunique()
)

st.divider()

# ==========================================================
# Column Names
# ==========================================================

st.subheader("📌 Column Names")

st.dataframe(
    pd.DataFrame({
        "Columns": df.columns
    }),
    use_container_width=True
)

st.divider()

# ==========================================================
# Data Types
# ==========================================================

st.subheader("📊 Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype_df, use_container_width=True)

st.divider()

# ==========================================================
# Missing Values
# ==========================================================

st.subheader("❌ Missing Values")

missing_df = pd.DataFrame({
    "Column": df.columns,
    "Missing Values": df.isnull().sum()
})

st.dataframe(
    missing_df,
    use_container_width=True
)

st.divider()

# ==========================================================
# Numerical Statistics
# ==========================================================

st.subheader("📈 Numerical Statistics")

st.dataframe(
    df.describe(),
    use_container_width=True
)

st.divider()

# ==========================================================
# Dataset Information
# ==========================================================

st.subheader("ℹ️ Dataset Information")

st.info(
    f"""
    • Total Rows : **{df.shape[0]}**

    • Total Columns : **{df.shape[1]}**

    • Dataset Size : **{round(df.memory_usage(deep=True).sum()/1024,2)} KB**

    • Target Column : **Rating**
    """
)