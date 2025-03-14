import streamlit as st
import pandas as pd
from yahooquery import Screener, Ticker

st.title("Market Screeners")
st.sidebar.image("img.png", use_container_width=True)

# Dictionary of available screeners
screeners = {
    "Most Active Stocks": "most_actives",
    "Top Gainers": "day_gainers",
    "Top Losers": "day_losers",
    "Undervalued Large Caps": "undervalued_large_caps",
    "High-Growth Technology Stocks": "growth_technology_stocks"
}

# Helper function to format Market Cap
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

# Select screener type
screener_name = st.selectbox("Select a screener:", list(screeners.keys()))

if screener_name:
    screener = Screener()
    screener_type = screeners[screener_name]
    results = screener.get_screeners(screener_type, count=10)

    if results and screener_type in results:
        stocks = results[screener_type]["quotes"]

        # Process stock list and format market cap
        stock_list = []
        for stock in stocks:
            formatted_market_cap = format_market_cap(stock.get("marketCap", "N/A"))
            stock_list.append({
                "Symbol": stock["symbol"],
                "Name": stock["shortName"],
                "Price": stock["regularMarketPrice"],
                "% Change": stock["regularMarketChangePercent"],
                "Market Cap": formatted_market_cap
            })

        # Display table
        df = pd.DataFrame(stock_list)
        df = df.astype(str)  # Fix PyArrow serialization issue
        st.write(f"**{screener_name}**")
        st.table(df)

        # Select stock for details
        selected_stock = st.selectbox("Select a stock to view details:", df["Symbol"])

        if selected_stock:
            stock = Ticker(selected_stock)
            market_cap = stock.summary_detail.get(selected_stock, {}).get("marketCap", "N/A")
            
            data = {
                "Company Name": stock.price.get(selected_stock, {}).get("longName", "N/A"),
                "Market Cap": format_market_cap(market_cap),  # Apply formatting
                "Current Price": stock.price.get(selected_stock, {}).get("regularMarketPrice", "N/A"),
                "P/E Ratio": stock.summary_detail.get(selected_stock, {}).get("trailingPE", "N/A"),
                "Sector": stock.asset_profile.get(selected_stock, {}).get("sector", "N/A"),
                "Industry": stock.asset_profile.get(selected_stock, {}).get("industry", "N/A"),
            }

            # Convert to DataFrame and fix serialization error
            df_details = pd.DataFrame(list(data.items()), columns=["Metric", "Value"])
            df_details["Value"] = df_details["Value"].astype(str)
            
            st.write(f"**Details for {selected_stock}:**")
            st.table(df_details)

