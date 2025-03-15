import streamlit as st
from yahooquery import Ticker
import pandas as pd

# Set up the Streamlit app
st.title("📈 Stock Trading Signal App")
st.write("""
- Slide down the side panel to select stock and parameters.
""")


# Sidebar for user input
st.sidebar.header("🔍 Select Stock and Parameters")

# Stock symbol input
SYMBOL = st.sidebar.text_input("Enter Stock Symbol (e.g., NVDA, AAPL, TSLA):", "NVDA").upper()

# Time Interval Selection
INTERVAL_OPTIONS = ["1h", "1d", "5d", "1wk", "1mo", "3mo"]
INTERVAL = st.sidebar.selectbox("Select Time Interval", INTERVAL_OPTIONS)

# **📌 NEW: Use sliders instead of dropdowns for more flexibility**
# Price Change Selection (0.1% to 10%)
PRICE_CHANGE_THRESHOLD = st.sidebar.slider("Select Price Change Threshold (%)", 0.1, 10.0, 0.5, step=0.1)

# Volume Multiplier Selection (1.0x to 3.0x)
VOLUME_MULTIPLIER = st.sidebar.slider("Select Volume Multiplier", 1.0, 3.0, 1.5, step=0.1)

# Run Analysis Button
if st.sidebar.button("📊 Run Analysis"):
    st.sidebar.success("Fetching Data and Calculating Signals...")

    # Check if the stock exists
    stock = Ticker(SYMBOL)
    stock_info = stock.asset_profile

    if SYMBOL not in stock_info or stock_info[SYMBOL] is None:
        st.error("🚨 No stock available. Please enter a valid stock symbol!")
    else:
        # Fetch historical data
        hist = stock.history(period="1y", interval=INTERVAL).reset_index()

        # **✅ Fix: Check if the DataFrame is empty before proceeding**
        if hist.empty:
            st.error(f"🚨 No historical data available for {SYMBOL}. Please try another stock!")
        else:
            # Convert 'date' column only if data exists
            hist["date"] = hist["date"].astype(str)

            # Calculate % Price Change from Previous Period
            hist["Price_Change"] = (hist["close"] - hist["close"].shift(1)) / hist["close"].shift(1) * 100

            # Calculate Volume Change (Compare with Previous Volume)
            hist["Volume_Change"] = hist["volume"] / hist["volume"].shift(1)

            # Default Signal
            hist["Signal"] = "HOLD"

            # Buy Signal: Price Change Up + Volume Spike
            hist.loc[
                (hist["Price_Change"] >= PRICE_CHANGE_THRESHOLD) & (hist["Volume_Change"] >= VOLUME_MULTIPLIER),
                "Signal"
            ] = "BUY"

            # Sell Signal: Price Change Down + Volume Spike
            hist.loc[
                (hist["Price_Change"] <= -PRICE_CHANGE_THRESHOLD) & (hist["Volume_Change"] >= VOLUME_MULTIPLIER),
                "Signal"
            ] = "SELL"

            # Display Results
            latest_signal = hist.iloc[-1]["Signal"]
            latest_price = hist.iloc[-1]["close"]
            latest_volume = hist.iloc[-1]["volume"]
            latest_pct_change = hist.iloc[-1]["Price_Change"]
            latest_volume_change = hist.iloc[-1]["Volume_Change"]

            st.subheader(f"📢 Latest Signal for {SYMBOL}: **{latest_signal}**")
            st.write(f"**📌 Latest Price:** ${latest_price:.2f}")
            st.write(f"📊 **Volume:** {latest_volume:,}")
            st.write(f"📈 **% Change in Price:** {latest_pct_change:.2f}%")
            st.write(f"📉 **Volume Change Multiplier (Compared to Previous Period):** {latest_volume_change:.2f}x (1.0 = No Change)")

            # Show last 5 signals in reverse order with price & volume change
            st.write(f"🔹 **Recent Signals ({INTERVAL} Interval):**")
            st.dataframe(hist[["date", "close", "Price_Change", "Volume_Change", "Signal"]].tail(5).iloc[::-1])  # Reverse order

            # Option to Run Again
            if st.button("🔄 Run Another Analysis"):
                st.experimental_rerun()

