import streamlit as st
import pandas as pd
from datetime import datetime
import base64

def set_bg():
    with open("assets/bg.jpg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    page_bg = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* make text readable */
    .stMetric, .stDataFrame, .stTable {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        padding: 10px;
    }}
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

set_bg()


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Amazon Price Tracker",
    page_icon="📦",
    layout="wide"
)

st.title("📦 Amazon Price Tracker Dashboard")

# ---------------- LOAD CSV ----------------
try:
    df = pd.read_csv("price_history.csv", header=None)
    df.columns = ["Date", "Product", "Price"]
except:
    st.error("No data found yet!")
    st.stop()

# ---------------- SIDEBAR ----------------
st.sidebar.header("Dashboard Info")
st.sidebar.write("Last Refresh:")
st.sidebar.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# ---------------- CLEAN PRICE ----------------
df["Price"] = df["Price"].astype(str).str.replace(",", "").astype(float)

# ---------------- METRICS ----------------
latest_price = df.iloc[-1]["Price"]
min_price = df["Price"].min()
max_price = df["Price"].max()

col1, col2, col3 = st.columns(3)

col1.metric("Latest Price", f"₹{latest_price}")
col2.metric("Lowest Price", f"₹{min_price}")
col3.metric("Highest Price", f"₹{max_price}")

st.divider()

# ---------------- TABLE ----------------
st.subheader("📋 Price History Table")
st.dataframe(df, use_container_width=True)

st.divider()

# ---------------- CHART ----------------
st.subheader("📈 Price Trend")
st.line_chart(df["Price"])
