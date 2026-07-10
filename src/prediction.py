import joblib

# Load trained model
model = joblib.load("models/rating_prediction_model.pkl")

print("Flipkart Product Rating Prediction")

review = input("Enter a product review: ")

prediction = model.predict([review])

print("\nPredicted Rating:", prediction[0])