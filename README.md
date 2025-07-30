# Book Web Scraper

A Python web scraper that extracts book information from [Books to Scrape](http://books.toscrape.com/).

## Features

- **Interactive Genre Selection**: Choose from 56 different book genres
- **Comprehensive Book Information**: Extracts and displays title, rating, price, and link for each book
- **User-Friendly Output**: Displays books in a numbered, formatted list
- **Robust Error Handling**: Uses regular expressions for reliable data extraction

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Blue00FF/Book_Scraper_Project.git
   cd Book_Scraper_Project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the scraper:
   ```bash
   python Book_Scraper.py
   ```

2. Select a genre from the interactive menu

3. View book information displayed in the console

## Example Output

```
Book 1 of 20
Title: A Light in the Dark
Rating: Three stars
Price: £19.24
Link: http://books.toscrape.com/catalogue/a-light-in-the-dark_21/index.html

Book 2 of 20
Title: Tipping the Velvet
Rating: Four stars
Price: £5.76
Link: http://books.toscrape.com/catalogue/tipping-the-velvet_19/index.html
```

## Dependencies

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/): HTML parsing
- [PyInputPlus](https://pyinputplus.readthedocs.io/): User input with validation
- [Requests](https://docs.python-requests.org/): HTTP requests
- [Regex](https://docs.python.org/3/library/re.html): Regular expressions for data extraction

## Project Structure

```
Book_Scraper_Project/
├── Book_Scraper.py          # Main scraping script
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files
└── LICENSE                 # License information
```

## Potential Improvements

- Add support for pagination to scrape more than just the first page of books
- Implement error handling for network requests
- Add command-line arguments for non-interactive use
- Save results to a file (CSV, JSON, etc.)
- Add unit tests for the scraping functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Documentation

For comprehensive codebase analysis and additional documentation, see the [AGENTS.md](AGENTS.md) file.

## Current Status

- The project is functional and successfully extracts book information
- All dependencies are properly installed
- The script works as expected with interactive genre selection
- The license has been updated to MIT
- The AGENTS.md file provides comprehensive documentation of the codebase

 
