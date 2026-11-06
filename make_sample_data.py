"""Create a tiny SAMPLE dataset (not real reviews) to test the analysis scripts
without running the scraper:

    python make_sample_data.py
    python analyze_reviews.py data/sample_reviews.csv
"""
from pathlib import Path

import pandas as pd

Path("data").mkdir(exist_ok=True)

# These are made-up examples, NOT real Best Buy reviews
reviews = [
    {"review_id": "sample-1", "review_title": "Great battery",
     "review_body": "The battery lasts all day and the sound is excellent.",
     "review_date": "2026-10-20", "star_rating": 5,
     "source_platform": "Sample", "reviewer_name": "Sample User"},
    {"review_id": "sample-2", "review_title": "Stopped working",
     "review_body": "The left ear cup stopped working after a week. Very disappointed.",
     "review_date": "2026-10-21", "star_rating": 1,
     "source_platform": "Sample", "reviewer_name": "Example User"},
    {"review_id": "sample-3", "review_title": "Okay",
     "review_body": "Terrible fit, it hurts my ears.",
     "review_date": "2026-10-22", "star_rating": 4,
     "source_platform": "Sample", "reviewer_name": "Example User 2"},
]

df = pd.DataFrame(reviews)
df.to_csv("data/sample_reviews.csv", index=False)

print(df)
print("\nSample dataset saved to data/sample_reviews.csv")
