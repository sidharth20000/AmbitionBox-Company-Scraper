# AmbitionBox Company Scraper

This Python script scrapes company information from AmbitionBox and stores it in a MongoDB database.

## Features

- Scrapes company data from multiple pages of AmbitionBox
- Extracts information such as company name, rating, reviews, domain, location, duration, and number of employees
- Stores the scraped data in a MongoDB database

## Requirements

- Python 3.x
- BeautifulSoup4
- requests
- pymongo

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ambitionbox-scraper.git
   cd ambitionbox-scraper
   ```

2. Install the required packages:
   ```
   pip install beautifulsoup4 requests pymongo
   ```

3. Ensure you have MongoDB installed and running on your local machine.

## Usage

1. Run the script:
   ```
   python AmbitionBox.py
   ```

2. The script will scrape data from 333 pages of AmbitionBox and store it in a MongoDB database named `Ambition_Box` in a collection called `Companies_Information`.

## Data Structure

The script collects the following information for each company:

- Name
- Rating
- Number of Reviews
- Domain
- Location
- Duration (presumably the company's age)
- Number of Employees

## Note

This script is for educational purposes only. Please be respectful of AmbitionBox's terms of service and robots.txt file. Consider implementing proper rate limiting and error handling for production use.
