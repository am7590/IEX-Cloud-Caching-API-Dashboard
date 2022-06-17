import streamlit as st
import config
import redis
import json
from iex import IEXStock

redis_client = redis.Redis(host='localhost', port=6379, db=0)
symbol = st.sidebar.text_input("Symbol", value="AAPL")
stock = IEXStock(config.IEX_KEY, symbol)

screen = st.sidebar.selectbox("View", ("Overview", "Fundamentals", "News", "Ownership", "Dividends", "Insider "                                                                                            "Transactions"))
st.title(screen)

if screen == "Overview":
    logo_key = f"{symbol}_logo"
    logo = redis_client.get(logo_key)

    if logo is None:
        print("Retrieving data from API...")
        logo = stock.get_logo()
        redis_client.set(logo_key, json.dumps(logo))
    else:
        print("Retrieving data from cache...")
        logo = json.loads(logo)

    company_key = f"{symbol}_company"
    company_info = redis_client.get(company_key)

    if company_info is None:
        print("Retrieving data from API...")
        company_info = stock.get_company_info()
        redis_client.set(company_key, json.dumps(company_info))
    else:
        print("Retrieving data from cache...")
        company_info = json.loads(company_info)

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
    stats_key = f"{symbol}_stats"
    stats = redis_client.get(stats_key)

    if stats is None:
        print("Retrieving data from API...")
        stats = stock.get_stats()
        redis_client.set(stats_key, json.dumps(stats))
    else:
        print("Retrieving data from cache...")
        stats = json.loads(stats)

    st.write(stats)

if screen == "News":
    news_key = f"{symbol}_news"
    news = redis_client.get(news_key)

    if news is None:
        print("Retrieving data from API...")
        news = stock.get_company_news(25)
        redis_client.set(news_key, json.dumps(news))
    else:
        print("Retrieving data from cache...")
        news = json.loads(news)

    st.write(news)

if screen == "Ownership":
    institutional_ownership_key = f"{symbol}_ownership"
    institutional_ownership = redis_client.get(institutional_ownership_key)

    if institutional_ownership is None:
        print("Retrieving data from API...")
        institutional_ownership = stock.get_institutional_ownership()
        redis_client.set(institutional_ownership_key, json.dumps(institutional_ownership))
    else:
        print("Retrieving data from cache...")
        institutional_ownership = json.loads(institutional_ownership)

    st.write(institutional_ownership)

if screen == "Dividends":
    dividends_key = f"{symbol}_dividends"
    dividends = redis_client.get(dividends_key)

    if dividends is None:
        print("Retrieving data from API...")
        dividends = stock.get_dividends()
        redis_client.set(dividends_key, json.dumps(dividends))
    else:
        print("Retrieving data from cache...")
        dividends = json.loads(dividends)

    st.write(dividends)

if screen == "Insider Transactions":
    insider_transactions_key = f"{symbol}_insider_transactions"
    insider_transactions = redis_client.get(insider_transactions_key)

    if insider_transactions is None:
        print("Retrieving data from API...")
        insider_transactions = stock.get_insider_transactions()
        redis_client.set(insider_transactions_key, json.dumps(insider_transactions))
    else:
        print("Retrieving data from cache...")
        insider_transactions = json.loads(insider_transactions)

    st.write(insider_transactions)
