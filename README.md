##Web Scraper

This is a basic Python web scraper that extracts data from web pages and saves it to a CSV file. The scraper uses `requests` for making HTTP requests, `BeautifulSoup` for parsing HTML, and `csv` to save the extracted data.

Features

- Fetches web pages via HTTP requests.
- Extracts the title, links, and paragraphs from each page.
- Saves the extracted data to a CSV file.
- Handles HTTP errors and logs them for debugging.
- Provides customizable delays between requests to prevent overloading the server.

Requirements

- Python 3.x
- `requests` library
- `BeautifulSoup4` library (part of `bs4`)
- `logging` (standard Python library)
- `csv` (standard Python library)

You can install the required libraries using pip:

pip install requests beautifulsoup4

Usage

Initialize the Web Scraper

To use the scraper, instantiate a `WebScraper` object with the base URL and optional delay between requests:

scraper = WebScraper(base_url="https://example.com", delay=1)

- `base_url`: The root URL of the website you want to scrape.
- `delay`: The time (in seconds) to wait between requests (default is 1 second).

Scrape URLs

You can specify a list of relative URLs (e.g., `"/about"`, `"/contact"`) to scrape:

urls_to_scrape = ["/", "/about", "/contact"]
scraper.scrape(urls_to_scrape, "output.csv")

- `urls`: A list of relative URLs you want to scrape.
- `output_file`: The filename to save the extracted data (default is `scraped_data.csv`).

CSV Output

The extracted data includes the following fields:

- `title`: The title of the page.
- `links`: A list of all links (href attributes) on the page.
- `paragraphs`: A list of text from all paragraphs on the page.

The data is saved to a CSV file with the following columns: `title`, `links`, and `paragraphs`.

Example Output

A sample CSV output might look like this:

title,links,paragraphs
"Home","['/about', '/contact']",["Welcome to our website!", "This is the home page."]

Error Handling and Logging

The scraper logs any errors encountered during the scraping process, such as network issues or parsing errors. Logs are written to the console with timestamps.

Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. Make sure to follow the Python code style and include tests for any new features.

License

This project is open source and available under the MIT License (LICENSE).
