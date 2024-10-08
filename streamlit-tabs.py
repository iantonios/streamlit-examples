import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://storage.googleapis.com/scsu-data-science/tips.csv'
df = pd.read_csv(url)
df['tip_pct'] = df['tip'] / df['total_bill'] * 100
st.title('Restaurant spending')

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

tab1, tab2 = st.tabs(["Bill amount", "Tips"])

with tab1:
   st.pyplot(fig1)

with tab2:
   st.pyplot(fig2)
