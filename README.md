# Job-Ads-Analyzer

Job Ads Analyzer is a tool that allows users to analyze and explore job advertisements data. It provides features for viewing job trends, filtering ads, sorting, and more. This README provides information on how to use and install the project.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [License](#license)

## Features
- Word Cloud for job titles
- Distribution plots for date posted and count of job ads
- Filtering and sorting job ads based on different criteria
- Distribution of job ads by the date companies were founded
- Displaying job and company data in the terminal
- more...

## Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:SemirBaldzhiev/Job-Ads-Analyzer.git
    cd Job-Ads-Analyzer
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up the database:
    - Initialize your SQLite database with job ads and company data.
    ```bash
    cd src/dbsqlite
    python3 create_tables.py
    cd ../../
    ```
4. Scrape data for job ads and companies
    - This commands will take more time for execution
    ```bash
    cd src/scraper
    python3 company_scraper.py
    python3 ads_scraper.py
    ```

## Usage
1. Run the Job Ads Analyzer CLI (from project directory):
    ```bash
    python main.py
    ```
2. Follow the on-screen instructions to log in or register.
3. Use the available commands to analyze job ads data.

## Tests
1. Run all test with the following command (from project directory):
    ```bash
    python3 test.py
    ```

## License
This project is licensed under the [Apache License](LICENSE).

