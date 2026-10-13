# Books Data Analytics

## Project Overview

This project explores book data through web scraping, exploratory data analysis (EDA), data visualization, and an interactive dashboard built with Python.

It demonstrates practical data analytics skills, including data collection, cleaning, analysis, visualization, and interactive reporting.

### Live Dashboard

Explore the interactive dashboard online:

**[Open Books Analysis Dashboard](https://basma-books-dashboard.streamlit.app/)**

The dashboard allows users to search and filter books, explore price and rating distributions, and view book details through interactive charts.

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

- **Average book price:** Approximately £38.05.
- **Price range:** £13.99–£57.25.
- **Average rating:** 2.85 out of 5.
- One-star books were the most common rating category in this sample.
- The Pearson correlation between price and rating was approximately -0.076, indicating no clear linear relationship in this small sample.
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

## Project Structure

```text
Books_Data_Analytics/
├── app.py
├── scraper.py
├── eda.py
├── eda.ipynb
├── books.csv
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/BasmaMohamed123/Books_Data_Analytics.git
cd Books_Data_Analytics
```

### 2. Install the Required Libraries

```bash
python -m pip install -r requirements.txt
```

### 3. Run the Web Scraper

```bash
python scraper.py
```

This generates or updates `books.csv`.

### 4. Run the EDA Script

```bash
python eda.py
```

### 5. Open the Visualization Notebook

```bash
jupyter notebook eda.ipynb
```

Run all notebook cells to view the visualizations.

### 6. Run the Interactive Dashboard

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL where you can open and interact with the dashboard.

Alternatively, access the deployed dashboard online:

**[Open Live Dashboard](https://basma-books-dashboard.streamlit.app/)**

## GitHub Repository

**[View Source Code on GitHub](https://github.com/BasmaMohamed123/Books_Data_Analytics)**

