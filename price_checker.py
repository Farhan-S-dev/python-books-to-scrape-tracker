# =========================================================
# PROJECT 3: Price Checker with Random Delay
# What this project does: checks a page's price again and again,
# tells us when it changes, and saves a log of every check.
# Why we built it this way: real scraping/automation gigs need
# random pauses between checks so we don't hammer a website too fast.
# =========================================================

import requests   # what: lets python go fetch a webpage, like a browser does
                   # why: we need this to actually get the price data from the site

import time        # what: lets us pause the program
                    # why: so we don't hit the website too fast, too many times

import random       # what: gives us random numbers
                     # why: we use this to make the pause time different every round, not a fixed number

from datetime import datetime   # what: gives us the current date and time
                                 # why: so we can note down WHEN we checked the price, like a log

from bs4 import BeautifulSoup   # what: this is the tool that reads/understands the page structure (like reading HTML)
                                 # why: raw page text is messy, this helps us pick out just the price part


# ---------------------------------------------------------
# SETTINGS - the page we're watching
# ---------------------------------------------------------
URL = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
# what: this is the page we are going to check again and again
# why: we need one fixed page to track, so we can compare price today vs price next check


def get_price():
    # what: this function's only job is - go to the page, find the price, bring it back
    # why: we keep this separate so our main loop stays clean and simple

    response = requests.get(URL)
    # what: this actually downloads the page content
    # why: without this we have no data to read from

    soup = BeautifulSoup(response.text, "html.parser")
    # what: this turns the raw page into something we can search through easily

    price = soup.find("p", class_="price_color").text
    # what: this finds the exact tag where the price is written, and takes its text
    # why: this is the ONE piece of information we actually care about

    return price
    # what: sends the price back to whoever called this function


def log_price(price):
    # what: this function writes the price + time into a text file
    # why: so later we have a record of every check, not just the current one

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # what: formats today's date and time into a readable string

    with open("price_log.txt", "a") as file:
        # what: opens our log file in "add" mode (a = append, doesn't erase old data)
        # why: we want to keep building the history, not overwrite it each time

        file.write(f"{now} - Price: {price}\n")
        # what: writes one line - the time and the price - into the file


def main():
    # what: this is the main runner that keeps everything looping
    # why: keeping this separate from the top-level code is a clean habit for real projects

    last_price = None
    # what: this variable remembers the price from the last check
    # why: so we can compare "is this new price different from before"

    while True:
        # what: this makes the program repeat forever, until we stop it manually
        # why: a price checker needs to keep checking, not just run once

        current_price = get_price()
        # what: calls our function above to get today's price

        if current_price != last_price:
            # what: checks if the price changed since last time
            # why: we only care about CHANGES, not repeating the same info again and again

            print(f"Price changed! New price: {current_price}")
            log_price(current_price)
            # what: prints it on screen AND saves it to file
            # why: screen = for us to see right now, file = for keeping a permanent record

            last_price = current_price
            # what: updates our "memory" so next time we compare against this new price

        else:
            print("No change in price.")
            # what: just tells us nothing changed, so we know the script is alive and working

        sleep_time = random.uniform(5, 15)
        # what: picks a random number of seconds between 5 and 15
        # why: this is the KEY part of this whole project - real gigs need random pauses
        #      so the website doesn't think it's a robot hammering it every exact 10 seconds

        print(f"Waiting {round(sleep_time, 1)} seconds before next check...")
        time.sleep(sleep_time)
        # what: pauses the program for that random number of seconds
        # why: this is literally the "random time.sleep" trick you wanted to learn


if __name__ == "__main__":
  # What: Try running the main loop, but catch the user pressing Ctrl + C gracefully
  # Why: Prevents ugly error traces and lets the script exit cleanly.
  try:
    main()
  except KeyboardInterrupt:
    print("\n[!] Price checker stopped manually by user. Have a great day!")