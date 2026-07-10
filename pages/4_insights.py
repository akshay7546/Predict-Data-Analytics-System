import streamlit as st
import pandas as pd

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="Business Insights",
    page_icon="💡",
    layout="wide"
)

st.title("💡 Business Insights Dashboard")

# --------------------------------
# Load Dataset
# --------------------------------
df = pd.read_csv("output/cleaned_data.csv")

# --------------------------------
# KPI Cards
# --------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("⭐ Average Rating", round(df["Rating"].mean(), 2))
col2.metric("📝 Total Reviews", len(df))
col3.metric("📦 Products", df["Product_name"].nunique())
col4.metric("🏆 Highest Rating", df["Rating"].max())

st.divider()

# --------------------------------
# Rating Distribution
# --------------------------------
st.subheader("⭐ Rating Distribution")

rating_count = df["Rating"].value_counts().sort_index()

st.dataframe(
    rating_count.reset_index().rename(
        columns={"index": "Rating", "Rating": "Reviews"}
    ),
    use_container_width=True
)

st.divider()

# --------------------------------
# Top Reviewed Products
# --------------------------------
st.subheader("🏆 Top 10 Most Reviewed Products")

top_products = (
    df["Product_name"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_products.columns = ["Product", "Reviews"]

st.dataframe(top_products, use_container_width=True)

st.divider()

# --------------------------------
# Business Insights
# --------------------------------
st.subheader("📈 Key Business Insights")

st.success("""
✅ Most customers give 4★ or 5★ ratings.

✅ Overall customer satisfaction is high.

✅ Positive reviews frequently mention:
- Performance
- Battery
- Display
- Value for Money

✅ Negative reviews often mention:
- Heating
- Battery Issues
- Delivery Problems
- Build Quality

✅ Improving these areas can increase customer satisfaction.
""")

st.divider()

# --------------------------------
# Business Recommendations
# --------------------------------
st.subheader("🚀 Business Recommendations")

st.info("""
1️⃣ Improve battery backup.

2️⃣ Reduce heating issues.

3️⃣ Improve delivery experience.

4️⃣ Maintain high product quality.

5️⃣ Continue focusing on performance and value for money.
""")

st.divider()

# --------------------------------
# Conclusion
# --------------------------------
st.subheader("📌 Final Conclusion")

st.write("""
The analysis shows that most customers are satisfied with the products.

The average rating is above 4 stars, indicating a positive customer experience.

Machine Learning successfully predicts customer ratings based on review text, helping businesses understand customer sentiment automatically.
""")