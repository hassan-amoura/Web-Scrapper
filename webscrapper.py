import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
from time import sleep
import logging

class WebScraper:
    def __init__(self, base_url, delay=1):
    
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def get_page(self, url):
        
        try:
            sleep(self.delay) 
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            self.logger.error(f"Error fetching {url}: {str(e)}")
            return None

    def extract_data(self, soup):
      
        data = {
            'title': soup.find('title').text.strip() if soup.find('title') else '',
            'links': [a.get('href') for a in soup.find_all('a', href=True)],
            'paragraphs': [p.text.strip() for p in soup.find_all('p')]
        }
        return data

    def save_to_csv(self, data, filename):
        
        if not data:
            self.logger.warning("No data to save")
            return

        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            self.logger.info(f"Data saved to {filename}")
        except IOError as e:
            self.logger.error(f"Error saving to CSV: {str(e)}")

    def scrape(self, urls, output_file='scraped_data.csv'):
       
        all_data = []
        
        for url in urls:
            full_url = urljoin(self.base_url, url)
            self.logger.info(f"Scraping {full_url}")
            
            soup = self.get_page(full_url)
            if soup:
                data = self.extract_data(soup)
                all_data.append(data)
            
        self.save_to_csv(all_data, output_file)

# Example usage
if __name__ == "__main__":
    scraper = WebScraper("")
    
    urls_to_scrape = [
        "/",
        "/about",
        "/contact"
    ]
    
    scraper.scrape(urls_to_scrape, "output.csv")