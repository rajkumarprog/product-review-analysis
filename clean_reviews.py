"""Remove duplicates, empty reviews and invalid ratings from the raw review CSV."""
import sys
from pathlib import Path

import pandas as pd

INPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/bestbuy_reviews_raw.csv")
OUTPUT = Path("data/cleaned_reviews.csv")

df = pd.read_csv(INPUT)
df = df.rename(columns={"body": "review_body", "rating": "star_rating"})

print("Original number of reviews:", len(df))

# Remove duplicate rows
df = df.drop_duplicates(subset=["review_id"] if "review_id" in df else None)

# Remove reviews with missing or empty text
df = df.dropna(subset=["review_body"])
df["review_body"] = df["review_body"].astype(str).str.strip()
df = df[df["review_body"] != ""]

# Keep only valid star ratings from 1 to 5
df["star_rating"] = pd.to_numeric(df["star_rating"], errors="coerce")
df = df[df["star_rating"].between(1, 5)]

print("Reviews after cleaning:", len(df))

df.to_csv(OUTPUT, index=False)
print(f"Cleaned dataset saved to {OUTPUT}")
