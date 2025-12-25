import streamlit as st 
import plotly.express as px
import pandas as pd
import yfinance as yf

st.title("Stock Data Viewer")
st.write("My first Streamlit App to view stock data using yfinance.")

ticker_symbol = st.text_input("Enter a ticker Symbol (e.g., AAPL, MSFT):").upper()

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Please enter a starting date")
with col2:
    end_date = st.date_input("Please enter an end date")

# ✅ Button
run_button = st.button("Get Stock Data")

# ✅ Code runs ONLY after button click
if run_button:
    if ticker_symbol == "":
        st.error("Please enter a ticker symbol.")
    elif start_date >= end_date:
        st.error("Start date must be before end date.")
    else:
        try:
            ticker_data = yf.Ticker(ticker_symbol)
            ticker_df = ticker_data.history(start=start_date, end=end_date)

            if ticker_df.empty:
                st.warning("No data found for given inputs.")
            else:
                st.subheader(f"{ticker_symbol}'s stock data in USD:")
                st.dataframe(ticker_df)

                st.title("Share's Closing Price Chart")
                st.line_chart(ticker_df["Close"])

                st.title("Share's Volume of Shares Traded each Day")
                st.line_chart(ticker_df["Volume"])

        except Exception as e:
            st.error(f"Error fetching data: {e}")

st.title("Thank You! for visiting our App")
