import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()


def send_telegram(msg):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chat_id, "text": msg}
        requests.get(url, params=params)
    except:
        print("Telegram send failed")




try:
    URL = "https://www.amazon.in/Apple-iPad-11%E2%80%B3-Display-All-Day/dp/B0DZ79Q1DB"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }

    response = requests.get(URL, headers=headers)
    if response.status_code != 200:
        raise Exception(f"HTTP Error {response.status_code}")

    if "captcha" in response.text.lower():
        raise Exception("Amazon CAPTCHA triggered")
    soup = BeautifulSoup(response.content, "lxml")

    # -------- TITLE --------
    title_tag = soup.find("span", id="productTitle")
    if title_tag:
        full_title = title_tag.get_text().strip()
        title = full_title.split(",")[0]
    else:
        title = "Unknown Product"

    print("Product:", title)

    # -------- PRICE --------
    # -------- PRICE --------
    price = None

    price_whole = soup.find("span", class_="a-price-whole")
    price_fraction = soup.find("span", class_="a-price-fraction")

    if price_whole and price_fraction:
        price = price_whole.text + price_fraction.text
    else:
        price_tag = soup.find("span", class_="a-offscreen")
        if price_tag:
            price = price_tag.text.replace("₹", "").strip()

    if price:
        print("Current Price:", price)

        # -------- SAVE LATEST PRICE TXT --------
        with open("price.txt", "w", encoding="utf-8") as f:
            f.write(price)

        # -------- DATE --------
        today = datetime.now().strftime("%Y-%m-%d")

        # -------- CSV HISTORY --------
        with open("price_history.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([today, title, price])

        # -------- PRICE COMPARISON --------
        target_price = 33000
        numeric_price = float(price.replace(",", ""))

        if numeric_price < target_price:
            print("Price Dropped!")
            send_telegram(f"Price dropped for {title}! Now: {price}")
        else:
            print("Price is still high")

    else:
        print("Price not found")


except Exception as e:
    error_message = f"Tracker Error: {str(e)}"
    print(error_message)
    send_telegram(error_message)
