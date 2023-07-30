import streamlit as st
import yfinance as yf

st.write("""
    # Stock Price Analysis""")

# get data for Apple

symbol = "TSLA"

# symbol = st.selectbox("Select symbol", "AAPL", "GOOG", "TSLA", "NFLX")

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d", start="2019-01-01", end="2022-12-31")
# ticker_df = ticker_data.history(period="1d")

st.write("""
    ### stock price data""")

st.dataframe(ticker_df)
st.line_chart(ticker_df["Close"])