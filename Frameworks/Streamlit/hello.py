import streamlit as st
import pandas as pd
import numpy as np

st.title('Apps')

st.write("""
#My first app with streamlit
Hello *Laurens!*
""")

##Columns
df = pd.DataFrame({
	'first column': ['Agro','Inbev','Tesla','Microsoft'],
	'second column': [10,20,30,40]
})



##Chart
chart_data = pd.DataFrame(
	np.random.randn(20,3),
	columns=['a','b','c']
)
st.line_chart(chart_data)

##Plot
# map_data = pd.DataFrame(
# 	np.random.randn(1000, 2) / [50,50] + [37.76, -120.4],
# 	columns=['lat', 'lon']
# )
# st.map(map_data)

option = st.sidebar.selectbox(
	'Which number do you like best?',
	df['first column'])
'You selected:', option