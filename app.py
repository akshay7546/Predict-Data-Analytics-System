import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Predict Data Analytics System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("📊 Navigation")
st.sidebar.success("Predict Data Analytics System")

st.sidebar.markdown("---")
st.sidebar.write("Developed by")
st.sidebar.write("**Akshay Kumar**")

# -----------------------------
# Main Title
# -----------------------------
st.title("📊 Predict Data Analytics System")

st.markdown("""
### Welcome 👋

This project analyzes Flipkart product reviews using Data Analytics and Machine Learning.

### Features

- 📂 Dataset Analysis
- 📊 Interactive Visualization
- 🤖 Rating Prediction
- 💡 Business Insights

---
""")

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Dataset", "Flipkart")
col2.metric("Rows", "2304")
col3.metric("Columns", "4")
col4.metric("ML Model", "Logistic Regression")

st.success("Project is ready for analysis.")