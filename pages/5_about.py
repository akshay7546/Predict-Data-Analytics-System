import streamlit as st

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

# --------------------------------
# Title
# --------------------------------
st.title("ℹ️ About This Project")

st.markdown("---")

# --------------------------------
# Project Overview
# --------------------------------
st.header("📊 Project Overview")

st.write("""
The **Predict Data Analytics System** is a Data Science and Machine Learning project
developed to analyze Flipkart product reviews and predict customer ratings based on review text.

This project helps businesses understand customer feedback, identify trends,
and make better business decisions using data analytics.
""")

st.markdown("---")

# --------------------------------
# Objectives
# --------------------------------
st.header("🎯 Project Objectives")

st.markdown("""
- Analyze customer reviews.
- Clean and preprocess real-world data.
- Visualize customer review patterns.
- Predict product ratings using Machine Learning.
- Generate business insights for better decision-making.
""")

st.markdown("---")

# --------------------------------
# Technologies Used
# --------------------------------
st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
### Programming
- Python
- Pandas
- NumPy
- Scikit-learn
""")

with col2:
    st.markdown("""
### Visualization & Dashboard
- Streamlit
- Plotly
- Matplotlib
""")

st.markdown("---")

# --------------------------------
# Machine Learning Model
# --------------------------------
st.header("🤖 Machine Learning Model")

st.info("""
Model Used:
• Logistic Regression

Text Vectorization:
• TF-IDF Vectorizer

Prediction Target:
• Product Rating (1–5 Stars)
""")

st.markdown("---")

# --------------------------------
# Dataset Information
# --------------------------------
st.header("📂 Dataset Information")

st.success("""
Dataset Name : Flipkart Product Reviews

Records : 2181

Features :
• Product Name
• Review
• Rating
""")

st.markdown("---")

# --------------------------------
# Developer
# --------------------------------
st.header("👨‍💻 Developer")

st.write("""
**Name:** Akshay Kumar

**Course:** B.Tech – Data Science

**Project:** Predict Data Analytics System
""")

st.markdown("---")

# --------------------------------
# Thank You
# --------------------------------
st.header("🙏 Thank You")

st.write("""
Thank you for exploring this project.

This dashboard demonstrates how Data Analytics and Machine Learning
can be used together to gain meaningful insights from customer reviews.
""")