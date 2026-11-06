# Product Review & Text Analysis

Python data-analysis project with two parts:

1. **Review scraping and sentiment analysis** – collects Best Buy Canada product reviews with Playwright, cleans them, and tags sentiment and product aspects.
2. **EDA and text mining on vehicle repair records** – a Jupyter notebook that cleans ~1,000 free-text repair records, tags issue types, and groups similar complaints with TF-IDF + K-Means clustering.

> Built as a timed machine-learning assessment. Part 1 is **partially complete** (see Status).

## Skills demonstrated

- Web scraping with Playwright and BeautifulSoup
- Data cleaning and de-duplication with pandas
- Exploratory data analysis and visualization (matplotlib)
- Rule-based multi-label text tagging
- TF-IDF vectorization and K-Means clustering (scikit-learn)
- Writing a stakeholder report from analysis results

## Part 1 – Review scraping and sentiment

| File | Purpose |
|---|---|
| `collect_bestbuy_reviews.py` | Opens the product page in Chromium and saves review cards to CSV |
| `extract_reviews.py` | Alternative: parse reviews from a product page saved as HTML |
| `clean_reviews.py` | Remove duplicates, empty text and invalid ratings |
| `analyze_reviews.py` | VADER (lexicon-based) sentiment, plus a flag when sentiment disagrees with the star rating |
| `make_sample_data.py` | Creates 3 made-up reviews to test the scripts without scraping |

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt
playwright install chromium

python collect_bestbuy_reviews.py     # writes data/bestbuy_reviews_raw.csv
python clean_reviews.py
python analyze_reviews.py             # writes data/bestbuy_reviews_with_sentiment.csv
```

Quick test without scraping:

```bash
python make_sample_data.py
python analyze_reviews.py data/sample_reviews.csv
```

Outputs are written to `data/`. Scraper selectors depend on the live website and may need updating.

## Part 2 – EDA and text mining

Open the notebook:

```bash
jupyter notebook HanuAI_Task2_EDA_TextMining.ipynb
```

Steps in the notebook: data-quality checks → text cleaning → descriptive EDA → rule-based issue tagging → inferred repair strategy → TF-IDF + K-Means clustering → export of the enriched dataset (`HanuAI_Task2_Analyzed_Dataset.csv`) and chart (`hanuai_issue_tags.png`).

![Issue tags](hanuai_issue_tags.png)

## Status

- Part 2: complete (notebook, enriched dataset, chart, stakeholder report)
- Part 1: scripts work, but only 10 unique reviews were collected against a target of 50; sentiment is a heuristic baseline, not a trained model

## Known issues / next steps

- Replace the lexicon sentiment baseline with a trained classifier and report accuracy
- Move scripts into a `src/` folder
- Add aspect tagging (battery, comfort, sound…) to the review pipeline

## Author

**Rajkumar Panikera** · [LinkedIn](https://www.linkedin.com/in/rajkumar-panikera-a083ab1a5) · [GitHub](https://github.com/rajkumarprog)
