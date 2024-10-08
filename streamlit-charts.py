# Illustrates adding figures in Streamlit

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

url = 'https://storage.googleapis.com/scsu-data-science/kc_house_data.csv'
df = pd.read_csv(url)

cols = ['price', 'sqft_living', 'yr_built', 'lat', 'long']
df_short = df.loc[:100, cols]
df_short = df_short.rename(columns={'long': 'lon'})

st.subheader('Kent county (WA) dataset')
st.dataframe(df_short, width = 800, height = 200)

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(df_short['sqft_living'], df_short['price']/1000, s=10)
ax.set_xlabel('Living Sq. Ft')
ax.set_ylabel('Price (in $1,000)')
st.subheader('\nRelationship between living space and price')
st.pyplot(fig = fig, clear_figure=True)

# DataFrame must contain columns named 'lon' and 'lat'
st.map(df_short)
