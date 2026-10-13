
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Books Analysis Dashboard",
    page_icon="📚",
    layout="wide"
)

# Load the dataset from the project folder
DATA_PATH = Path(__file__).parent / "books.csv"

st.title("📚 Books Analysis Dashboard")
st.write(
    "An interactive dashboard exploring book prices, ratings, "
    "and availability using data collected from Books to Scrape."
)

if not DATA_PATH.exists():
    st.error("books.csv was not found. Run scraper.py first.")
    st.stop()

# Read and clean the dataset
df = pd.read_csv(DATA_PATH)

df["Price"] = (
    df["Price"]
    .astype("string")
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)
df = df.dropna(subset=["Price", "Rating"]).copy()

if df.empty:
    st.error("No valid book data is available for analysis.")
    st.stop()

# Sidebar filters
st.sidebar.header("Filter Books")

search = st.sidebar.text_input("Search by book title")

rating_options = sorted(df["Rating"].unique().tolist())

selected_ratings = st.sidebar.multiselect(
    "Filter by rating",
    options=rating_options,
    default=rating_options,
    format_func=lambda rating: f"{int(rating)} star"
)

min_price = float(df["Price"].min())
max_price = float(df["Price"].max())

price_range = st.sidebar.slider(
    "Price range (£)",
    min_value=min_price,
    max_value=max_price,
    value=(min_price, max_price),
    step=0.01
)

filtered_df = df[
    df["Rating"].isin(selected_ratings)
    & df["Price"].between(price_range[0], price_range[1])
].copy()

if search:
    filtered_df = filtered_df[
        filtered_df["Title"].str.contains(
            search, case=False, na=False
        )
    ]

# Key metrics
st.subheader("Dataset Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Books Found", len(filtered_df))
col2.metric(
    "Average Price",
    f"£{filtered_df['Price'].mean():.2f}"
    if not filtered_df.empty else "N/A"
)
col3.metric(
    "Average Rating",
    f"{filtered_df['Rating'].mean():.2f} / 5"
    if not filtered_df.empty else "N/A"
)
col4.metric(
    "In-Stock Books",
    int(
        filtered_df["Availability"]
        .str.contains("In stock", case=False, na=False)
        .sum()
    )
)

if filtered_df.empty:
    st.warning("No books match the selected filters.")
    st.stop()

# Rating distribution
st.subheader("Rating Distribution")

rating_counts = (
    filtered_df["Rating"]
    .value_counts()
    .reindex([1, 2, 3, 4, 5], fill_value=0)
    .rename_axis("Rating")
    .reset_index(name="Number of Books")
)

rating_chart = px.bar(
    rating_counts,
    x="Rating",
    y="Number of Books",
    title="Number of Books by Star Rating",
    labels={
        "Rating": "Rating (Stars)",
        "Number of Books": "Number of Books"
    },
    text="Number of Books"
)

rating_chart.update_xaxes(
    tickmode="array",
    tickvals=[1, 2, 3, 4, 5]
)
rating_chart.update_layout(
    xaxis_title="Rating (Stars)",
    yaxis_title="Number of Books"
)

st.plotly_chart(rating_chart, use_container_width=True)

# Price charts
left, right = st.columns(2)

with left:
    st.subheader("Book Price Distribution")

    price_chart = px.histogram(
        filtered_df,
        x="Price",
        nbins=8,
        title="Distribution of Book Prices",
        labels={"Price": "Price (£)"}
    )

    st.plotly_chart(price_chart, use_container_width=True)

with right:
    st.subheader("Price vs. Rating")

    scatter_chart = px.scatter(
        filtered_df,
        x="Rating",
        y="Price",
        hover_name="Title",
        title="Book Price Compared with Rating",
        labels={
            "Rating": "Rating (Stars)",
            "Price": "Price (£)"
        }
    )

    scatter_chart.update_xaxes(
        tickmode="array",
        tickvals=[1, 2, 3, 4, 5]
    )

    st.plotly_chart(scatter_chart, use_container_width=True)

# Filtered data table
st.subheader("Book Details")

display_df = filtered_df[
    ["Title", "Price", "Rating", "Availability", "URL"]
].copy()

display_df["Price"] = display_df["Price"].map(
    lambda price: f"£{price:.2f}"
)

display_df["Rating"] = display_df["Rating"].map(
    lambda rating: f"{int(rating)} / 5"
)

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "URL": st.column_config.LinkColumn("Book Link")
    }
)

st.caption(
    "Dataset scope: 20 books collected from the first page of "
    "Books to Scrape. Findings may not represent the entire website."
)
