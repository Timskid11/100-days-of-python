import requests
from bs4 import BeautifulSoup
import csv

# Website URL
url = "https://books.toscrape.com/"

# Send request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all book containers
books = soup.find_all("article", class_="product_pod")

# Create CSV file
with open("books_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price (£)", "Rating"])

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("£", "")
        rating = book.find("p", class_="star-rating")["class"][1]

        writer.writerow([title, price, rating])

print("Scraping completed. Data saved to books_data.csv")
