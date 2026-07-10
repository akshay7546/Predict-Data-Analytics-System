import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("output/cleaned_data.csv")

# Create output folder if it doesn't exist
import os
os.makedirs("output/figures", exist_ok=True)

# -----------------------------
# 1. Rating Distribution
# -----------------------------
plt.figure(figsize=(6,4))
df["Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/figures/rating_distribution.png")
plt.show()

# -----------------------------
# 2. Top 10 Most Reviewed Products
# -----------------------------
plt.figure(figsize=(10,6))
df["Product_name"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Most Reviewed Products")
plt.xlabel("Product Name")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("output/figures/top_products.png")
plt.show()

# -----------------------------
# 3. Review Length Distribution
# -----------------------------
df["Review_Length"] = df["Review"].apply(len)

plt.figure(figsize=(6,4))
plt.hist(df["Review_Length"], bins=20)
plt.title("Review Length Distribution")
plt.xlabel("Review Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/figures/review_length_distribution.png")
plt.show()

print("Visualizations saved successfully!")