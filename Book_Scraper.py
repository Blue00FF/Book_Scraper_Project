from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

base_url = "http://books.toscrape.com/"

base_html = urlopen(base_url).read().decode("utf-8")

base_soup = BeautifulSoup(base_html, "html.parser")

categories = base_soup.select("a[href^='catalogue/category/books/']")

travel_url = base_url + categories[0]["href"]

travel_html = urlopen(travel_url).read().decode("utf-8")

travel_soup = BeautifulSoup(travel_html, "html.parser")

travel_books = travel_soup.select("article")

print("Travel Books")

for i in range(len(travel_books)):

    title = re.search(
        'title="(?P<title>.*?)"', str(travel_books[i].select("a[title]")[0])
    ).group("title")

    rating = re.search(
        'class="star-rating (?P<rating>.*?)"',
        str(travel_books[i].select("p[class^='star']")[0]),
    ).group("rating")

    price = str(travel_books[i].select('p[class="price_color"]')[0])[23:29]

    print(
        f"""Book {i + 1} of {len(travel_books)}
        
        Title: {title}
        
        Rating: {rating} stars
        
        Price: {price}"""
    )
