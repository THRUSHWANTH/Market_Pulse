# import streamlit as st

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

# st.title("📈 Yahoo Finance Data Pull")

# st.write("""
# Welcome to the Yahoo Finance Data Pull application. Use the navigation menu to explore:

# - **Stock Company Info**: Retrieve information about specific companies.
# - **Market Index Info**: View details of major market indices.
# - **Market Screeners**: Discover top gainers, losers, and more.
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

st.title("MarketPulse 📈")

st.write("""
Welcome to the Yahoo Finance Data Pull application. Use the navigation menu to explore:

- **Stock Company Info**: Retrieve information about specific companies.
- **Market Index Info**: View details of major market indices.
- **Market Screeners**: Discover top gainers, losers, and more.
- **Market Summary**: Get an overview of the US market.
- **Trending Stocks**: View the latest trending stocks.
""")

# Display image using the correct parameter
st.sidebar.image("img.png", use_container_width=True)


