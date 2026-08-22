# Project 3: Books to Scrape - Real-time Stock Tracker

This project implements a web scraper to monitor product availability and pricing on the "Books to Scrape" website. It focuses on automation, anti-bot techniques, timing, and data logging.

## 🚀 What it does
- Scrapes product listing pages to monitor "in-stock" status and prices.
- Runs continuous checks using loops.
- Implements randomized delays to mimic human behavior and avoid rate limits.
- Timestamps and logs tracked data to local files.

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** `requests`, `BeautifulSoup4`, `time`, `random`, `datetime`

## 💡 Key Skills
- Web Scraping with `BeautifulSoup`.
- Building continuous monitoring loops with polite rate-limiting (`time.sleep` and `random`).
- Timestamping records using `datetime`.
- File I/O operations for automated data logging.