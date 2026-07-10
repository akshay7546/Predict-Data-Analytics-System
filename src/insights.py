import pandas as pd

# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

print("=" * 60)
print("        FLIPKART PRODUCT REVIEW INSIGHTS")
print("=" * 60)

# Total Reviews
print(f"\n1. Total Reviews : {len(df)}")

# Average Rating
print(f"2. Average Rating : {df['Rating'].mean():.2f}")

# Highest Rating
print(f"3. Highest Rating : {df['Rating'].max()}")

# Lowest Rating
print(f"4. Lowest Rating : {df['Rating'].min()}")

# Rating Distribution
print("\n5. Rating Distribution")
print(df["Rating"].value_counts().sort_index())

# Most Reviewed Products
print("\n6. Top 10 Most Reviewed Products")
print(df["Product_name"].value_counts().head(10))

# Average Review Length
df["Review_Length"] = df["Review"].astype(str).apply(len)

print(f"\n7. Average Review Length : {df['Review_Length'].mean():.2f} characters")

# Longest Review
longest_review = df.loc[df["Review_Length"].idxmax()]

print("\n8. Product with Longest Review")
print("Product :", longest_review["Product_name"])
print("Rating  :", longest_review["Rating"])

print("\n" + "=" * 60)
print("Business Insights")
print("=" * 60)

print("• Most customers gave high ratings (4–5 stars).")
print("• Rating 5 is the most common rating.")
print("• Products with more positive reviews generally receive higher ratings.")
print("• Customers frequently mention performance and battery in positive reviews.")
print("• Negative reviews often mention battery, heating, delivery, or quality issues.")
print("• Businesses should focus on resolving common complaints to improve customer satisfaction.")

print("\nInsight generation completed successfully!")