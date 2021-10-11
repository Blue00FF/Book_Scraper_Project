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

base_url = "http://books.toscrape.com/"

base_html = urlopen(base_url).read().decode("utf-8")

base_soup = BeautifulSoup(base_html, "html.parser")

user_choice = pyip.inputMenu(
    choices=categories_list,
    prompt="Please choose the genre you'd like to know more about. \n",
    numbered=True,
).lower()

user_choice = "-".join(user_choice.split())

print(user_choice)

categories_links = base_soup.select(
    "a[href^='catalogue/category/books/" + user_choice + "']"
)

genre_url = base_url + categories_links[0]["href"]

genre_html = urlopen(genre_url).read().decode("utf-8")

genre_soup = BeautifulSoup(genre_html, "html.parser")

genre_books = genre_soup.select("article")

for i in range(len(genre_books)):

    title = re.search(
        'title="(?P<title>.*?)"', str(genre_books[i].select("a[title]")[0])
    ).group("title")

    rating = re.search(
        'class="star-rating (?P<rating>.*?)"',
        str(genre_books[i].select("p[class^='star']")[0]),
    ).group("rating")

    price = str(genre_books[i].select('p[class="price_color"]')[0])[23:29]

    link = re.search(
        'href="../../../(?P<link>.*?)/index.html"',
        str(genre_books[i].find_all("h3")),
    ).group("link")

    link = base_url + "catalogue/" + link

    print(
        f"""Book {i + 1} of {len(genre_books)}
        
        Title: {title}
        
        Rating: {rating} stars
        
        Price: {price}
        
        Link: {link}"""
    )
