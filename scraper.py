
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Website URL
url = "https://books.toscrape.com/"

# Store scraped book data
data = []

try:
    # Send a request to the website
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    # Extract information from each book
    for book in books:
        title_element = book.select_one("h3 a")
        price_element = book.select_one(".price_color")
        rating_element = book.select_one(".star-rating")
        availability_element = book.select_one(
            ".instock.availability"
        )

        # Skip entries with missing required information
        if not all([
            title_element,
            price_element,
            rating_element,
            availability_element
        ]):
            continue

        title = title_element.get("title", "").strip()

        price = (
            price_element.get_text(strip=True)
            .replace("Â£", "£")
        )

        rating_classes = rating_element.get("class", [])
        rating = next(
            (item for item in rating_classes
             if item in ["One", "Two", "Three", "Four", "Five"]),
            None
        )

        availability = availability_element.get_text(
            " ", strip=True
        )

        book_url = urljoin(url, title_element.get("href", ""))

        # Add the book if its information is complete
        if title and price and rating and book_url:
            data.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "URL": book_url
            })

    # Check whether any books were extracted
    if not data:
        raise ValueError(
            "No books were extracted. Check the website HTML structure."
        )

    # Convert the extracted data into a DataFrame
    df = pd.DataFrame(data)

    # Save the dataset as a CSV file
    df.to_csv("books.csv", index=False, encoding="utf-8-sig")

    print("Scraping completed successfully!")
    print(f"Number of books extracted: {len(df)}")
    print("Dataset saved to: books.csv")
    print("\nPreview of the dataset:")
    print(df.head())

except requests.exceptions.RequestException as error:
    print(f"Website request failed: {error}")

except (ValueError, AttributeError, KeyError) as error:
    print(f"Data extraction failed: {error}")
