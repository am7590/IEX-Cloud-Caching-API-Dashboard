import streamlit as st
import requests
import config

symbol = st.sidebar.text_input("Symbol", value="AAPL")

screen = st.sidebar.selectbox("View", ("Overview", "Fundamentals", "News", "Ownership", "Technicals"))

st.write(symbol)

st.title(screen)

if screen == "Overview":
    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/logo?token={config.IEX_KEY}"
    r = requests.get(url)
    response = r.json()
    st.image(response['url'])

    url = f"https://cloud.iexapis.com/stable/stock/{symbol}/company?token={config.IEX_KEY}"
    r = requests.get(url)
    response = r.json()
    # st.write(response)

    st.write(response['companyName'])
    st.write(response['industry'])
    st.write(response['CEO'])


if screen == "Fundamentals":
    pass