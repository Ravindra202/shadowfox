@@ -1,50 +1,75 @@


import requests
from bs4 import BeautifulSoup
import csv
def scrape_shadowfox():
    url = "https://shadowfox.in"
import time
BASE_URL   = "https://books.toscrape.com/catalogue/"
START_URL  = "https://books.toscrape.com/catalogue/page-1.html"
OUTPUT_CSV = "books_toscrape.csv"
MAX_PAGES  = 50        # set to a lower number to scrape fewer pages
DELAY_SEC  = 0.5       # polite delay between requests

    headers = {
        "User-Agent": "Mozilla/5.0"
    }
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

    try:
        response = requests.get(url, headers=headers, timeout=10)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BookScraper/1.0; +https://example.com)"
}

        # Error handling for bad response
        response.raise_for_status()
def scrape_books(start_url: str, max_pages: int) -> list[dict]:
    books = []
    url   = start_url
    page  = 1

        soup = BeautifulSoup(response.text, "html.parser")
    while url and page <= max_pages:
        print(f"  Page {page:>2} → {url}")
        try:
            resp = requests.get(url, headers=HEADERS, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            print(f"  ERROR on page {page}: {e}")
            break

        # Extract data
        title = soup.title.text.strip() if soup.title else "No Title"
        headings = [tag.text.strip() for tag in soup.find_all(["h1", "h2"])]
        soup = BeautifulSoup(resp.text, "lxml")

        print("Website Title:", title)
        print("\nHeadings:")
        for h in headings:
            print("-", h)
        for article in soup.select("article.product_pod"):
            title   = article.h3.a["title"]
            raw_price = article.select_one("p.price_color").text.strip()
            price   = raw_price.encode("ascii", "ignore").decode()   
            rating  = RATING_MAP.get(article.p["class"][1], 0)
            avail   = article.select_one("p.availability").text.strip()
            rel_link = article.h3.a["href"].replace("../", "")
            link    = BASE_URL + rel_link

        # Save to CSV
        with open("shadowfox_data.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            books.append({
                "Title":             title,
                "Price (£)":         price,
                "Rating (out of 5)": rating,
                "Availability":      avail,
                "URL":               link,
            })

            writer.writerow(["Title"])
            writer.writerow([title])
      
        next_btn = soup.select_one("li.next a")
        url = BASE_URL + next_btn["href"] if next_btn else None
        page += 1
        time.sleep(DELAY_SEC)

            writer.writerow([])
            writer.writerow(["Headings"])
    return books

            for h in headings:
                writer.writerow([h])

        print("\n Data saved to shadowfox_data.csv")
def save_csv(books: list[dict], path: str) -> None:
    fieldnames = ["Title", "Price (£)", "Rating (out of 5)", "Availability", "URL"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(books)
    print(f"\n✓ Saved {len(books)} books to '{path}'")

    except requests.exceptions.RequestException as e:
        print(" Network Error:", e)

    except Exception as e:
        print(" Unexpected Error:", e)


scrape_shadowfox()
if __name__ == "__main__":
    print(f"Scraping books.toscrape.com (up to {MAX_PAGES} pages)...\n")
    books = scrape_books(START_URL, MAX_PAGES)
    save_csv(books, OUTPUT_CSV)
