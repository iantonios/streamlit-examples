# Illustrates use of columns container
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://storage.googleapis.com/scsu-data-science/tips.csv'
df = pd.read_csv(url)

st.title('Restaurant spending')
st.markdown('---')

st.subheader('The data')
st.dataframe(df, width = 600, height = 200)

df['tip_pct'] = df['tip'] / df['total_bill'] * 100

st.markdown('---')
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.set_xlabel('Bill ($)')
ax1.set_title('Bill amount distribution')
ax1.hist(df['total_bill'], bins = 20, color='red', alpha=0.5)

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.set_title('Tip amount distribution')
ax2.set_xlabel('Tips (%)')
ax2.hist(df['tip_pct'], bins = 20, color='blue', alpha=0.5)

col1, col2 = st.columns(2)

with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

st.markdown('---')
