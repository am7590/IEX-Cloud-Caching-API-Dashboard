import streamlit as st
import requests
import config
from iex import IEXStock

symbol = st.sidebar.text_input("Symbol", value="AAPL")

stock = IEXStock(config.IEX_KEY, symbol)

screen = st.sidebar.selectbox("View", ("Overview", "Fundamentals", "News", "Ownership", "Technicals"))
st.title(screen)

if screen == "Overview":
    logo = stock.get_logo()
    company_info = stock.get_company_info()

    col1, col2 = st.beta_columns([1, 3])

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


if screen == "Fundamentals":
    stats = stock.get_stats()
    st.write(stats)