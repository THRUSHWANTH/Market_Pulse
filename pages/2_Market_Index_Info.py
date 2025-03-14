import streamlit as st
from yahooquery import Ticker
import pandas as pd

st.title("📈 Market Index Info")
st.sidebar.image("img.png", use_container_width=True)

indices = {
    "S&P 500": "^GSPC",
    "Dow Jones": "^DJI",
    "Nasdaq": "^IXIC",
    "Russell 2000": "^RUT",
    "FTSE 100": "^FTSE",
    "Nikkei 225": "^N225"
}

index_name = st.selectbox("Select an index:", list(indices.keys()))

if index_name:
    index_symbol = indices[index_name]
    index = Ticker(index_symbol)
    data = {
        "Index Name": index.price.get(index_symbol, {}).get("longName", "N/A"),
        "Current Level": index.price.get(index_symbol, {}).get("regularMarketPrice", "N/A"),
        "Market Change %": index.price.get(index_symbol, {}).get("regularMarketChangePercent", "N/A"),
        "52-Week High": index.summary_detail.get(index_symbol, {}).get("fiftyTwoWeekHigh", "N/A"),
        "52-Week Low": index.summary_detail.get(index_symbol, {}).get("fiftyTwoWeekLow", "N/A"),
    }
    
    # Convert to DataFrame and format properly
    df = pd.DataFrame(data.items(), columns=["Metric", "Value"])
    st.table(df)  # Display as a proper table without extra row numbers



