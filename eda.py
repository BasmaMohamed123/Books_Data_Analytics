
"""
CodeAlpha - Exploratory Data Analysis (EDA)

Analyze the books dataset collected from the first page of
Books to Scrape.

Research questions:
1. What is the average book price?
2. Which books are the cheapest and most expensive?
3. How are ratings distributed?
4. Is book price associated with book rating?
5. Which rating category has the highest average price?

Hypothesis:
Higher-rated books may have higher prices.

Note:
The dataset contains only 20 books from the first page.
Results should not be generalized to the entire website.
"""

import pandas as pd

# 1. Load the dataset
df = pd.read_csv("books.csv")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

print("\nFirst five rows:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nDataset shape:", df.shape)

# 2. Clean and convert prices
df["Price"] = (
    df["Price"]
    .astype("string")
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# 3. Convert rating labels to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# 4. Check data quality
print("\n" + "=" * 50)
print("DATA QUALITY CHECK")
print("=" * 50)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

# Keep rows with valid prices and ratings for numerical analysis
analysis_df = df.dropna(subset=["Price", "Rating"]).copy()

if analysis_df.empty:
    raise ValueError(
        "No valid rows remain after cleaning. Check books.csv."
    )

print("\nValid rows for analysis:", len(analysis_df))

# 5. Summary statistics
print("\n" + "=" * 50)
print("PRICE AND RATING SUMMARY")
print("=" * 50)

print(f"\nAverage price: £{analysis_df['Price'].mean():.2f}")
print(f"Minimum price: £{analysis_df['Price'].min():.2f}")
print(f"Maximum price: £{analysis_df['Price'].max():.2f}")
print(f"Average rating: {analysis_df['Rating'].mean():.2f} / 5")

# 6. Find cheapest and most expensive books
cheapest = analysis_df.loc[analysis_df["Price"].idxmin()]
most_expensive = analysis_df.loc[analysis_df["Price"].idxmax()]

print("\nCheapest book:")
print(f"{cheapest['Title']} — £{cheapest['Price']:.2f}")

print("\nMost expensive book:")
print(f"{most_expensive['Title']} — £{most_expensive['Price']:.2f}")

# 7. Rating distribution
rating_counts = (
    analysis_df["Rating"]
    .value_counts()
    .sort_index()
    .reindex([1, 2, 3, 4, 5], fill_value=0)
)

print("\n" + "=" * 50)
print("RATING DISTRIBUTION")
print("=" * 50)

print(rating_counts)

# 8. Average price for each rating
average_price_by_rating = (
    analysis_df.groupby("Rating")["Price"]
    .mean()
    .reindex([1, 2, 3, 4, 5])
    .dropna()
)

print("\nAverage price by rating:")
print(average_price_by_rating.round(2))

if not average_price_by_rating.empty:
    highest_avg_rating = average_price_by_rating.idxmax()
    lowest_avg_rating = average_price_by_rating.idxmin()

    print(
        f"\nHighest average price: {highest_avg_rating:.0f}-star books "
        f"(£{average_price_by_rating.max():.2f})"
    )

    print(
        f"Lowest average price: {lowest_avg_rating:.0f}-star books "
        f"(£{average_price_by_rating.min():.2f})"
    )

# 9. Explore price-rating association
correlation = analysis_df["Price"].corr(analysis_df["Rating"])

print("\n" + "=" * 50)
print("PRICE AND RATING ASSOCIATION")
print("=" * 50)

print(f"Pearson correlation: {correlation:.3f}")

print(
    "Interpretation: Correlation describes the direction and strength "
    "of a linear association. This small sample cannot establish "
    "causation or support broad conclusions about all books."
)

# 10. Key insights
print("\n" + "=" * 50)
print("KEY INSIGHTS")
print("=" * 50)

print(f"- Dataset rows: {len(df)}")
print(f"- Valid rows analyzed: {len(analysis_df)}")
print(f"- Average price: £{analysis_df['Price'].mean():.2f}")
print(f"- Average rating: {analysis_df['Rating'].mean():.2f} / 5")

most_common_rating = rating_counts.idxmax()

print(f"- Most common rating: {most_common_rating}-star")

print(
    "- Scope: 20 books were originally collected from the first page "
    "of the website."
)
