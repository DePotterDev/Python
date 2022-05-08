import yfinance as yf
import streamlit as st
from datetime import date
import pandas as pd


today = date.today().strftime("%Y-%m-%d")

st.write("""
    # Currency in Brazilian Real
""")

euroBrl = yf.Ticker("EURBRL=X")
usdBrl = yf.Ticker("USDBRL=X")
gbpBrl = yf.Ticker("GBPBRL=X")

euro = euroBrl.history(period='1d', start='2010-1-1', end=today)
usd = usdBrl.history(period='1d', start='2010-1-1', end=today)
gbp = gbpBrl.history(period='1d', start='2010-1-1', end=today)


df = pd.DataFrame({
	'first column': ['EURO','USD','GBP'],
})

option = st.sidebar.selectbox(
    'Select other currency.',
    df['first column']
)
'You selected:', option

eurFiftyDayAverage = euroBrl.info['fiftyDayAverage']
eurTwoHunderdDayAverage = euroBrl.info['twoHundredDayAverage']
eurRegularMarketPrice = euroBrl.info['regularMarketPrice']

usdFiftyDayAverage = usdBrl.info['fiftyDayAverage']
usdTwoHunderdDayAverage = usdBrl.info['twoHundredDayAverage']
usdRegularMarketPrice = usdBrl.info['regularMarketPrice']

gbpFiftyDayAverage = gbpBrl.info['fiftyDayAverage']
gbpTwoHunderdDayAverage = gbpBrl.info['twoHundredDayAverage']
gbpRegularMarketPrice = gbpBrl.info['regularMarketPrice']

if option == 'EURO':
    st.write("""
        ### Closing Prices *EURO/BRL*
        **Market Price:** """, eurRegularMarketPrice,
        """**50 day average:**""", eurFiftyDayAverage,
        """**200 day average:**""", eurTwoHunderdDayAverage
        )
    st.line_chart(euro.Close)
if option == 'USD':
    st.write("""
        ### Closing Prices *USD/BRL*
        **Market Price:** """, usdRegularMarketPrice,
        """**50 day average:**""", usdFiftyDayAverage,
        """**200 day average:**""", usdTwoHunderdDayAverage
        )
    st.line_chart(usd.Close)
    st.text(usdBrl.info)
if option == 'GBP':
    st.write("""
        ### Closing Prices *GBP/BRL*
        **Market Price:** """,gbpRegularMarketPrice,
        """**50 day average:**""",gbpFiftyDayAverage,
        """**200 day average:**""",gbpTwoHunderdDayAverage
        )
    st.line_chart(gbp.Close)