

"""Book Scraper: A script to scrape book information from an online bookstore."""

import re
from urllib.request import urlopen

import pyinputplus as pyip
from bs4 import BeautifulSoup

categories_list = [
    "Travel",
    "Mystery",
    "Historical Fiction",
    "Sequential Art",
    "Classics",
    "Philosophy",
    "Romance",
    "Womens Fiction",
    "Fiction",
    "Childrens",
    "Religion",
    "Nonfiction",
    "Music",
    "Science Fiction",
    "Sports and Games",
    "Fantasy",
    "New Adult",
    "Young Adult",
    "Science",
    "Poetry",
    "Paranormal",
    "Art",
    "Psychology",
    "Autobiography",
    "Parenting",
    "Adult Fiction",
    "Humor",
    "Horror",
    "History",
    "Food and Drink",
    "Christian Fiction",
    "Business",
    "Biography",
    "Thriller",
    "Contemporary",
    "Spirituality",
    "Academic",
    "Self Help",
    "Historical",
    "Christian",
    "Suspense",
    "Short Stories",
    "Novels",
    "Health",
    "Politics",
    "Cultural",
    "Erotica",
    "Crime",
]

BASE_URL = "http://books.toscrape.com/"

with urlopen(BASE_URL) as response:
    base_html = response.read().decode("utf-8")

base_soup = BeautifulSoup(base_html, "html.parser")

USER_CHOICE = pyip.inputMenu(
    choices=categories_list,
    prompt="Please choose the genre you'd like to know more about. \n",
    numbered=True,
).lower()

USER_CHOICE = "-".join(USER_CHOICE.split())

print(USER_CHOICE)

categories_links = base_soup.select(
    "a[href^='catalogue/category/books/" + USER_CHOICE + "']"
)

genre_url = BASE_URL + categories_links[0]["href"]

with urlopen(genre_url) as response:
    genre_html = response.read().decode("utf-8")

genre_soup = BeautifulSoup(genre_html, "html.parser")

genre_books = genre_soup.select("article")

for i, book in enumerate(genre_books):

    title = re.search(
        'title="(?P<title>.*?)"', str(book.select("a[title]")[0])
    ).group("title")

    rating = re.search(
        'class="star-rating (?P<rating>.*?)"',
        str(book.select("p[class^='star']")[0]),
    ).group("rating")

    PRICE = str(book.select('p[class="price_color"]')[0])[23:29]

    link = re.search(
        'href="../../../(?P<link>.*?)/index.html"',
        str(book.find_all("h3")),
    ).group("link")

    link = BASE_URL + "catalogue/" + link

    print(
        f"""Book {i + 1} of {len(genre_books)}

        Title: {title}

        Rating: {rating} stars

        Price: {PRICE}

        Link: {link}"""
    )
