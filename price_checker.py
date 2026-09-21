import requests
import time
import random
from datetime import datetime
from bs4 import BeautifulSoup

URL = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


def get_price():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find("p", class_="price_color").text
    return price


def log_price(price):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("price_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{now} - Price: {price}\n")


def main():
    last_price = None

    while True:
        current_price = get_price()

        if current_price != last_price:
            print(f"Price changed! New price: {current_price}")
            log_price(current_price)
            last_price = current_price
        else:
            print("No change in price.")

        sleep_time = random.uniform(5, 15)

        print(f"Waiting {round(sleep_time, 1)} seconds before next check...")
        time.sleep(sleep_time)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Price checker stopped manually by user. Have a great day!")
