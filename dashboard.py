import streamlit as st
import requests
import config
import redis
from iex import IEXStock

redis_client = redis.Redis(host='localhost', port=6379, db=0)

symbol = st.sidebar.text_input("Symbol", value="AAPL")

stock = IEXStock(config.IEX_KEY, symbol)

screen = st.sidebar.selectbox("View", ("Overview", "Fundamentals", "News", "Ownership", "Dividends", "Insider "
                                                                                                     "Transactions"))
st.title(screen)

if screen == "Overview":
    logo = stock.get_logo()
    company_info = stock.get_company_info()

    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(logo['url'])

    with col2:
        st.subheader(company_info['companyName'])
        st.subheader("Description")
        st.write(company_info['description'])
        st.subheader("Industry")
        st.write(company_info['industry'])
        st.subheader("CEO")
        st.write(company_info['CEO'])

        st.write(company_info)

if screen == "Fundamentals":
    stats = stock.get_stats()
    st.write(stats)

if screen == "News":
    news = stock.get_company_news(25)
    st.write(news)

if screen == "Ownership":
    institutional_ownership = stock.get_institutional_ownership()
    st.write(institutional_ownership)

if screen == "Dividends":
    dividends = stock.get_dividends()
    st.write(dividends)

if screen == "Insider Transactions":
    insider_transactions = stock.get_insider_transactions()
    st.write(insider_transactions)