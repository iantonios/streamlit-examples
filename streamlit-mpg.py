import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Car gas consumption')
df = pd.read_csv('https://storage.googleapis.com/scsu-data-science/mpg.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

st.markdown('---')
st.subheader('Gas consumption by country of origin')

origin = st.radio('Select country of origin', ('US', 'Europe', 'Japan'))

if origin == 'US':
    df = df.loc[df['origin']=='usa']
elif origin == 'Europe':
    df = df.loc[df['origin']=='europe']
else:
    df = df.loc[df['origin']=='japan']

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('mpg')
ax.hist(df['mpg'])
st.pyplot(fig)
