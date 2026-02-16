# 📦 Amazon Price Tracker with Dashboard

A Python-based Amazon Price Tracking system that monitors product prices, stores historical data, sends Telegram alerts on price drops, and displays trends in a Streamlit dashboard.

---

## 🚀 Features

- Scrapes Amazon product price automatically
- Stores daily price history in CSV
- Sends Telegram alert when price drops below target
- Interactive Streamlit Dashboard
- Beautiful UI with custom background
- Error handling for CAPTCHA / HTTP issues
- Secure credential management using `.env`

---

## 🛠 Tech Stack

- Python
- BeautifulSoup
- Requests
- Streamlit
- Pandas
- Telegram Bot API

---

## 📊 Dashboard Preview

- Latest Price
- Lowest Price
- Highest Price
- Price Trend Graph
- Historical Price Table

---

## 📂 Project Structure

```
amazon-price-tracker/
│
├── main.py              # Scraper & Telegram Alert
├── dashboard.py         # Streamlit UI
├── price_history.csv    # Stored price history
├── price.txt            # Latest price
├── assets/              # Background image folder
├── .env                 # Credentials (NOT pushed)
└── .gitignore
```

---

## 🔐 Environment Variables

Create a `.env` file:

```
TELEGRAM_TOKEN=your_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

---

## ▶ How to Run

### Install Dependencies
```
pip install requests beautifulsoup4 streamlit pandas python-dotenv
```

### Run Scraper
```
python main.py
```

### Run Dashboard
```
streamlit run dashboard.py
```

---

## ⚠ Notes

- Amazon may trigger CAPTCHA occasionally.
- Use delays or scheduling to avoid blocking.
- Credentials are hidden using `.env` for security.

---

## 👤 Author

**Ashiq Abbas**  
Aspiring Data Analyst | Python Developer  

---

## 🌟 Future Improvements

- Multi-product tracking
- Email notifications
- Public web interface
- Database storage
- Cloud deployment

---

## 📌 Purpose

This project demonstrates skills in:

- Web Scraping  
- Automation  
- Data Visualization  
- Secure Credential Handling  
- Dashboard Development  

---
