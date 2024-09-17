# Web Scraper

## Description

This is a Python-based web scraper designed to extract data from web pages. It fetches, parses, and saves HTML content including titles, paragraphs, and links.

## Features

- Fetches web page content using `requests`
- Parses HTML to extract titles, paragraphs, and links using `BeautifulSoup`
- Saves the extracted data to a JSON file
- Logs activities and errors using `logging`
- Customizable output file names

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install Dependencies:**

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. **Run the Scraper:**

    ```bash
    python webscraper.py "https://example.com" -o output.json
    ```

    Replace `"https://example.com"` with the URL you want to scrape and `output.json` with your desired output file name.

2. **View the Output:**

    The scraped data will be saved in the specified JSON file.

## Examples

- **Scrape a GeeksforGeeks Tutorial:**

    ```bash
    python webscraper.py "https://www.geeksforgeeks.org/python-web-scraping-tutorial/" -o output_geeksforgeeks.json
    ```

- **Scrape a CSO Online Article:**

    ```bash
    python webscraper.py "https://www.csoonline.com/article/3236449/what-is-cybersecurity.html" -o cybersecurity_output.json
    ```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact [your.email@example.com](mailto:your.email@example.com).
