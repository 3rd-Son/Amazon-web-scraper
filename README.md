# Web Scraping with Selenium and BeautifulSoup

This project demonstrates web scraping Amazon search results using Python, Selenium, and BeautifulSoup. It allows you to scrape information about any item from the Amazon search results and store the data in CSV format.

## Project Description

The purpose of this project is to provide a flexible and reusable web scraping solution for extracting information from Amazon search results. The script utilizes Selenium for automated web browsing and BeautifulSoup for parsing HTML data.

## Features

- Search for any item on Amazon and scrape the search results.
- Extract relevant information such as product description, price, rating, review counts, URL, and image.
- Store the extracted data in a CSV file for further analysis.

## Dependencies

Make sure you have the following dependencies installed:

- Python: Install Python from the [official Python website](https://www.python.org/downloads/).
- Selenium: Install Selenium by running `pip install selenium` in your terminal.
- BeautifulSoup: Install BeautifulSoup by running `pip install beautifulsoup4` in your terminal.
- Chrome WebDriver: Download the Chrome WebDriver executable compatible with your Chrome browser version. You can find it on the [official ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Setup

Follow these steps to set up the project:

1. Clone the project repository or download the source code.
2. Install the required dependencies mentioned above.
3. Place the Chrome WebDriver executable in a location accessible by your Python environment and update the path in the script accordingly.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the script by executing the command `python automated-scrap.py`.
3. Enter the item you want to scrape when prompted.
4. The script will scrape the Amazon search results for the provided item and extract relevant information, such as description, price, rating, review counts, URL, and image.
5. The extracted data will be stored in a CSV file named `results.csv` in the project directory.

## Contributing

Contributions to the project are welcome! If you have any ideas, suggestions, or bug fixes, feel free to submit a pull request or open an issue on the project repository.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
