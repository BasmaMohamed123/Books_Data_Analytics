# CodeAlpha Data Science Internship

## Project Overview

This repository contains three data science tasks completed as part of the CodeAlpha Data Science Internship. The project covers web scraping, exploratory data analysis (EDA), data visualization, and an interactive dashboard built with Python.

## Tasks

### Task 1: Web Scraping

**File:** `scraper.py`

- Scraped book information from [Books to Scrape](https://books.toscrape.com/).
- Used Requests and BeautifulSoup to extract book data.
- Collected book titles, prices, ratings, availability, and URLs.
- Saved the extracted data to `books.csv` using Pandas.
- Added basic error handling for website requests and missing data.

### Task 2: Exploratory Data Analysis (EDA)

**File:** `eda.py`

- Inspected the dataset structure and data types.
- Cleaned prices and converted ratings into numerical values.
- Checked for missing values and duplicate rows.
- Calculated average, minimum, and maximum book prices.
- Analyzed rating distribution and average prices by rating.
- Explored the relationship between book prices and ratings using Pearson correlation.
- Summarized the main findings and dataset limitations.

### Task 3: Data Visualization

**File:** `eda.ipynb`

Created visualizations using Pandas and Matplotlib:

- Bar chart showing the distribution of book ratings.
- Scatter plot exploring the relationship between price and rating.
- Histogram showing the distribution of book prices.
- Key insights summarizing the visualization results.

### Interactive Dashboard

**File:** `app.py`

Built an interactive dashboard using Streamlit and Plotly.

Dashboard features:

- Key metrics, including book count, average price, average rating, and in-stock books.
- Search books by title.
- Filter books by rating and price range.
- Interactive rating distribution chart.
- Interactive book price distribution histogram.
- Interactive price-versus-rating scatter plot.
- Filtered book details table with links to the original book pages.

## Dataset

The dataset contains 20 books scraped from the first page of Books to Scrape.

**Columns:**

- `Title`
- `Price`
- `Rating`
- `Availability`
- `URL`

## Key Findings

- Average book price: approximately **£38.05**.
- Price range: **£13.99–£57.25**.
- Average rating: **2.85 out of 5**.
- One-star books were the most common rating category in this sample.
- The Pearson correlation between price and rating was approximately **-0.076**, indicating no clear linear relationship in this small sample.
- Three-star books had the highest average price, while four-star books had the lowest average price.

**Limitation:** These findings describe only 20 books collected from the first page of the website. They should not be generalized to all books on the website.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Jupyter Notebook
- Streamlit
- Plotly

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install the required libraries

```bash
python -m pip install -r requirements.txt
```

### 3. Run the web scraper

```bash
python scraper.py
```

This generates or updates `books.csv`.

### 4. Run the EDA script

```bash
python eda.py
```

### 5. Open the visualization notebook

```bash
jupyter notebook eda.ipynb
```

Run all notebook cells to view the visualizations.

### 6. Run the interactive dashboard

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL where you can open and interact with the dashboard.

## Internship

Completed as part of the CodeAlpha Data Science Internship, October–November 2026.
