# Books to Scrape Price Tracker

A Python price-monitoring script that repeatedly checks one product page on Books to Scrape and logs price changes with timestamps.

## What It Does

- Sends requests to a single book product page
- Extracts the current price with BeautifulSoup
- Compares the current price with the previous check
- Logs price changes with a timestamp
- Waits for a random interval between checks
- Stops cleanly when interrupted with Ctrl+C

## Project Files

```text
price_checker.py
price_log.txt
requirements.txt
README.md
```

## Requirements

- Python 3
- requests
- beautifulsoup4

Install the required packages with:

```bash
pip install -r requirements.txt
```

## How to Run

Run:

```bash
python price_checker.py
```

The script keeps checking the product price until you stop it manually with Ctrl+C.

When a price change is detected, it appends a line to:

```text
price_log.txt
```

Example:

```text
2026-08-18 07:26:12 - Price: £51.77
```

## Purpose

This project was built to practice repeated requests, functions, loops, timestamps, file logging, and simple price-change detection.

## Limitations

- It monitors only one product page.
- It tracks price only, not stock availability.
- It runs locally and must remain open to continue checking.
- It does not send email, SMS, or other notifications.
