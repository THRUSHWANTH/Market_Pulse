# import streamlit as st
# from yahooquery import Ticker, Screener
# import pandas as pd

# # Fix sidebar height using CSS
# st.markdown(
#     """
#     <style>
#     [data-testid="stSidebarContent"] {
#         height: 100vh !important;  /* Ensures sidebar fills the screen height */
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("MarketPulse 📈")

# st.write("""
# Welcome to the Yahoo Finance Data Pull application. Use the navigation menu to explore:

# - **Market Screeners**: Discover top gainers, losers, and more.
# - **Market Index Info**: View details of major market indices.
# - **Market Summary**: Get an overview of the US market.
# - **Trending Stocks**: View the latest trending stocks.
# - **Stock Company Info**: Retrieve information about specific companies.
# """)

# # Display image using the correct parameter
# st.sidebar.image("img.png", use_container_width=True)


import streamlit as st
from yahooquery import Ticker, Screener
import pandas as pd

# Fix sidebar height using CSS
st.markdown(
    """
    <style>
    [data-testid="stSidebarContent"] {
        height: 100vh !important;  /* Ensures sidebar fills the screen height */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main Title
st.title("MarketPulse 📈")

# Welcome Section
st.write("""
Welcome to **MarketPulse**, your go-to stock market analytics tool.  
Stay updated with real-time **market trends**, **stock insights**, and **financial data**.

Use the navigation menu on the left to explore:
""")

# Features List
st.markdown("""
### **🔍 Features**
- **📊 Market Screeners**: Discover top gainers, losers, and more.
- **📈 Market Index Info**: View details of major market indices.
- **📌 Market Summary**: Get an overview of the US market.
- **📌 Trending Stocks**: View the latest trending stocks.
- **🏢 Stock Company Info**: Retrieve information about specific companies.

---
""")

# Live Stock Market Status (Example: S&P 500)
st.subheader("📢 Market Snapshot: S&P 500 Index")
sp500 = Ticker("^GSPC")
index_price = sp500.price

# Display S&P 500 Live Data
if "^GSPC" in index_price:
    price = index_price["^GSPC"].get("regularMarketPrice", "N/A")
    change_percent = index_price["^GSPC"].get("regularMarketChangePercent", "N/A")
    st.metric(label="📈 S&P 500 Index Price", value=f"${price}", delta=f"{change_percent}%")
else:
    st.warning("⚠️ Unable to fetch live data. Please try again later.")

# About the App
st.markdown("""
### **Why Use MarketPulse?**
✅ **Real-time stock market data** for better decision-making.  
✅ **User-friendly interface** with clear insights.  
✅ **100% Free & Open Source** for everyone.  

---

📌 **Explore the tabs on the left to start analyzing stocks now!**  
""")

# Sidebar Content
st.sidebar.image("img.png", use_container_width=True)
st.sidebar.markdown("""
### **MarketPulse 📊**
Stay informed with real-time stock insights, market summaries, and trending stocks.
- Navigate through different sections using the sidebar.
- Check live stock prices and financial data.
- Get the latest market trends in seconds.
""")



