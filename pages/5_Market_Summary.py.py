import streamlit as st
import yahooquery as yq
import pandas as pd

st.title("📊 Market Summary")
st.sidebar.image("img.png", use_container_width=True)
def get_market_summary():
    """Fetch market summary using yahooquery functions."""
    return yq.get_market_summary()

# Fetch and process market summary data
data = get_market_summary()

if data:
    # Extract relevant fields
    processed_data = []
    for entry in data:
        processed_data.append({
            "Symbol": entry.get("symbol", "N/A"),
            "Name": entry.get("shortName", "N/A"),
            "Current Price": entry.get("regularMarketPrice", {}).get("fmt", "N/A"),
            "Market Change (%)": entry.get("regularMarketChangePercent", {}).get("fmt", "N/A"),
            "Market State": entry.get("marketState", "N/A")
        })

    df_summary = pd.DataFrame(processed_data)
    st.table(df_summary)
else:
    st.write("No market summary data available.")

