import streamlit as st
import plotly.express as px
import pandas as pd

st.header('Fuel efficiency (1970-1982)')
df = pd.read_csv('https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/mpg.csv')
df.dropna(inplace=True)
fig = px.scatter(
    df,
    x="model_year",
    y="mpg",
    color="origin",
    hover_data=["name"],
)

event = st.plotly_chart(fig, key="mpg", on_select="rerun")

event.selection
