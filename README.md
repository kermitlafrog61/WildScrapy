# WildScrapy

WildScrapy is a powerful Scrapy spider designed to scrape product data from the popular e-commerce site, Wildberries, and store it in a PostgreSQL database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need the following installed on your machine:

- Python 3.8 or newer
- Google Chrome (for use with the Selenium webdriver)
- PostgreSQL
- Chrome Driver

### Installation

1. Clone this repository
```bash
git clone https://github.com/kermitlafrog61/WildScrapy.git
```
2. Install the required Python packages
```bash
cd WildScrapy
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
The Python packages required are:

 - Scrapy
 - psycopg2-binary
 - scrapyd
 - setuptools
 - scrapyd-client
 - selenium
 - webdriver-manager
 - python-decouple

3. Download the Chrome Driver that matches your installed Google Chrome version. This will be used with Selenium to simulate user scrolling.

4. Setup your PostgreSQL database. Make sure to keep track of your database name, user, and password as these will be needed later.

5. Copy the .env.template file and create a new .env file. Replace the placeholder values with your actual PostgreSQL database information and your path to the Chrome Driver.
```bash
cp .env.template .env
vim .env
```

### Running the spider
```bash
scrapy crawl wild
```
