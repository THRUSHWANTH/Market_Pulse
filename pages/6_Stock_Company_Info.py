import pandas as pd
import streamlit as st
from yahooquery import Ticker

st.title("Stock Company Info")
st.sidebar.image("img.png", use_container_width=True)

def format_market_cap(market_cap):
    """Converts market cap into a readable format (M, B, T)"""
    if market_cap is None or market_cap == "N/A":
        return "N/A"
    market_cap = float(market_cap)  # Convert to float
    if market_cap >= 1_000_000_000_000:
        return f"{market_cap / 1_000_000_000_000:.3f}T"  # Trillions
    elif market_cap >= 1_000_000_000:
        return f"{market_cap / 1_000_000_000:.3f}B"  # Billions
    elif market_cap >= 1_000_000:
        return f"{market_cap / 1_000_000:.3f}M"  # Millions
    return f"{market_cap:.2f}"  # Raw value if < 1M

ticker = st.text_input("Enter stock ticker (e.g., AAPL, TSLA):").upper()

if ticker:
    stock = Ticker(ticker)
    market_cap = stock.summary_detail.get(ticker, {}).get("marketCap", "N/A")
    
    data = {
        "Company Name": stock.price.get(ticker, {}).get("longName", "N/A"),
        "Market Cap": format_market_cap(market_cap),  # Apply formatting
        "Current Price": stock.price.get(ticker, {}).get("regularMarketPrice", "N/A"),
        "P/E Ratio": stock.summary_detail.get(ticker, {}).get("trailingPE", "N/A"),
        "Sector": stock.asset_profile.get(ticker, {}).get("sector", "N/A"),
        "Industry": stock.asset_profile.get(ticker, {}).get("industry", "N/A"),
    }

    # Convert dictionary to Pandas DataFrame
    df = pd.DataFrame(list(data.items()), columns=["Metric", "Value"])

    # Convert all values to string to avoid ArrowTypeError
    df["Value"] = df["Value"].astype(str)

    st.table(df)  # Display table




