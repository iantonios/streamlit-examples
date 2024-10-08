# Illustrates displaying tables and data in a dashboard
import pandas as pd
import streamlit as st

st.subheader('metrics using st.metric')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

url = 'https://storage.googleapis.com/scsu-data-science/tips.csv'
df = pd.read_csv(url)

st.subheader('st.dataframe, width = 600px, height = 200px')
st.dataframe(df, width = 600, height = 200)

st.subheader('st.table shows the contents of entire DataFrame')
st.table(data = df)
