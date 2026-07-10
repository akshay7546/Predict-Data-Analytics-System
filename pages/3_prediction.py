import streamlit as st
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Product Review Rating Prediction")

st.write(
    "Enter a customer review below and the trained Logistic Regression model "
    "will predict its rating."
)

st.divider()

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/rating_prediction_model.pkl")

# -----------------------------
# User Input
# -----------------------------
review = st.text_area(
    "✍️ Enter Product Review",
    height=180,
    placeholder="Example: This laptop has excellent performance and battery backup..."
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Predict Rating"):

    if review.strip() == "":
        st.warning("⚠ Please enter a review.")
    else:

        prediction = model.predict([review])[0]

        st.subheader("Prediction Result")

        if prediction == 5:
            st.success(f"⭐ Predicted Rating: {prediction}/5")
            st.balloons()

        elif prediction == 4:
            st.info(f"⭐ Predicted Rating: {prediction}/5")

        elif prediction == 3:
            st.warning(f"⭐ Predicted Rating: {prediction}/5")

        else:
            st.error(f"⭐ Predicted Rating: {prediction}/5")