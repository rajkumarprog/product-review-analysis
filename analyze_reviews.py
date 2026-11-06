"""Tag each collected review with a VADER (lexicon-based) sentiment label.

Input:  data/bestbuy_reviews_raw.csv   (created by collect_bestbuy_reviews.py)
Output: data/bestbuy_reviews_with_sentiment.csv
"""
import sys
from pathlib import Path

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

INPUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/bestbuy_reviews_raw.csv")
OUTPUT = Path("data/bestbuy_reviews_with_sentiment.csv")

if not INPUT.exists():
    raise SystemExit(f"{INPUT} not found. Run collect_bestbuy_reviews.py first.")

df = pd.read_csv(INPUT)

# The collector writes review_body/star_rating; extract_reviews.py writes body/rating.
df = df.rename(columns={"body": "review_body", "rating": "star_rating"})
df["star_rating"] = pd.to_numeric(df["star_rating"], errors="coerce")

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(review):
    compound = analyzer.polarity_scores(str(review))["compound"]
    if compound >= 0.05:
        return "positive"
    if compound <= -0.05:
        return "negative"
    return "neutral"


df["sentiment"] = df["review_body"].apply(get_sentiment)

# Flag reviews where the text sentiment disagrees with the star rating
high = df["star_rating"] >= 4
low = df["star_rating"] <= 2
df["needs_review"] = (high & (df["sentiment"] != "positive")) | (low & (df["sentiment"] != "negative"))

OUTPUT.parent.mkdir(exist_ok=True)
df.to_csv(OUTPUT, index=False)

print(df[["review_body", "star_rating", "sentiment", "needs_review"]])
print("\nSentiment counts:\n", df["sentiment"].value_counts().to_string())
print(f"\nSaved to {OUTPUT}")

print("\nReviews that need manual checking:")
print(df[df["needs_review"]][["review_body", "star_rating", "sentiment"]])
