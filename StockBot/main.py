"""
This is where the main work starts and the streamlit app as well.
"""

# import libraries
import streamlit as st
import numpy as np
import seaborn as sns
import requests
import joblib
from bot import StockBot, StockViz
from data import AlphaVantageAPI
from model import VolatilityModel



### Streamlit app configuration
st.set_page_config(page_title='StockBot', layout='wide')

# side bar (for the fetch data module)
st.sidebar.header('Fetch stock data')
symbol = st.sidebar.text_input('Enter Stock Symbol (e.g., AAPL):', 'TSLA')
interval = st.sidebar.text_input('Enter the time interval (e.g., 5min)', '5min')
output_size = st.sidebar.text_input('Which output format do you want? full/compact', 'full')

# instantiate and use the data scraper module
scraper = AlphaVantageAPI()
df = scraper.fetch_data(symbol)   # fetch stock data
#st.dataframe(df)

# sider bar (for the stock bot)
st.sidebar.header('Stock bot parameters')
short_window = st.sidebar.number_input('Enter the short window value (e.g. 20 for 20 days)', 2)
long_window = st.sidebar.number_input('Enter the long window value (e.g. 200 for 200 days)', 10)

# side bar for volatility predictions
st.sidebar.header('Volatility prediction')
start_date = st.sidebar.date_input('Forecast starts from?')
forecast_days = st.sidebar.number_input('Forecast days', 1)

# instantiate and use the stock bot (predict tradings)
bot = StockBot()
stockbot = bot.stockbot(dataset = df, short_window = short_window, long_window = long_window)

st.title(f'Moving Average Crossover Bot for {symbol}')

# instantiate the module to visualize the trading bot's predictions
viz = StockViz()
dashboard = viz.stockviz(data = df, short_window = short_window, long_window = long_window)
st.pyplot(dashboard)
st.set_option('deprecation.showPyplotGlobalUse', False)
Data, Prediction, StockNews = st.tabs(['Stock Data', 'Price Predictions', 'Stock News'])

with Data:
    st.header(f"This is the live data of {symbol}")
    st.dataframe(df)

with Prediction:
    st.header('Make Predictions About how your stock...')
    m = VolatilityModel(df['close']*100)
    forecast = m.forecast_stock_price(forecast_days = forecast_days, start_date = start_date)
    st.dataframe(forecast)

with StockNews:
    st.title("Get the latest news on your stock here...")
    from stocknews import StockNews
    sn = StockNews(symbol)
    news = sn.read_rss()
    for i in range(5):
        st.header(news['title'][i])
        st.write(news['published'][i])
        st.write(news['summary'][i])
        sentiment = news['sentiment_summary'][i]
        if sentiment >= 0:
            st.write('Sentiment: Positive')
        else:
            st.write('Sentiment: Negative')
        #st.write(news['title'][i])
        
