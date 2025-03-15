import streamlit as st
import yahooquery as yq
import pandas as pd

st.title("🔥 Trending Stocks")
st.sidebar.image("img.png", use_container_width=True)

def get_trending_stocks():
    """Fetch trending stocks using yahooquery functions."""
    trending_data = yq.get_trending()
    
    # Extract quotes directly from response
    if trending_data:
        return trending_data.get("quotes", [])
    
    return []

# Fetch and display trending stocks
trending_stocks = get_trending_stocks()

# Create a DataFrame
if trending_stocks:
    df_trending = pd.DataFrame(trending_stocks)
    st.table(df_trending)

