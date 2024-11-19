import streamlit as st
import pandas as pd

url = 'https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/tips.csv'
df = pd.read_csv(url)

values = st.slider(
    'Select a range of tip amounts',
    0.0, 20.0, (5.0, 15.0))

# Show rows with matching tip range 
df = df.loc[((df['tip'] > values[0]) & (df['tip'] < values[1])), :]
st.dataframe(df)
