import requests
from bs4 import BeautifulSoup
import logging
import argparse
import json
import os

# Set up logging
logging.basicConfig(filename='webscraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        """Fetch the webpage data."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            logging.info(f"Successfully fetched data from {self.url}")
            return response.content
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching webpage: {e}")
            return None

    def parse_data(self, html):
        """Parse the HTML data."""
        soup = BeautifulSoup(html, 'html.parser')
        data = {}

        # Extract title
        title = soup.title.text.strip() if soup.title else 'No title found'
        data['title'] = title
        logging.info(f"Extracted title: {title}")

        # Extract paragraphs
        paragraphs = [p.text.strip() for p in soup.find_all('p')]
        data['paragraphs'] = paragraphs
        logging.info(f"Extracted {len(paragraphs)} paragraphs.")

        # Extract links
        links = [link['href'] for link in soup.find_all('a', href=True)]
        data['links'] = links
        logging.info(f"Extracted {len(links)} links.")

        return data

    def save_to_file(self, data, filename):
        """Save the extracted data to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            logging.info(f"Data successfully saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving data to file: {e}")

def main():
    parser = argparse.ArgumentParser(description='Web Scraper')
    parser.add_argument('url', help='URL of the webpage to scrape')
    parser.add_argument('-o', '--output', default='output.json', help='Output file name (default: output.json)')
    args = parser.parse_args()

    scraper = WebScraper(args.url)
    html = scraper.fetch_data()
    if html:
        data = scraper.parse_data(html)
        scraper.save_to_file(data, args.output)

if __name__ == '__main__':
    main()
