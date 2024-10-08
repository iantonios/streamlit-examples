# Illustrates use of columns container
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://storage.googleapis.com/scsu-data-science/tips.csv'
df = pd.read_csv(url)
df['tip_pct'] = df['tip'] / df['total_bill'] * 100

st.title('Restaurant spending')
st.markdown('---')


col1, col2, col3 = st.columns(3)
with col1:
    meal = st.radio("Meal",('Lunch', 'Dinner'))
    if meal == 'Lunch':
        df = df.loc[df['time'] == 'Lunch']
    else:
        df = df.loc[df['time'] == 'Dinner']

with col2:
    smoker = st.radio("Smoker?",('Yes', 'No'))
    if smoker == 'Yes':
        df = df.loc[df['smoker'] == 'Yes']
    else:
        df = df.loc[df['smoker'] == 'No']

with col3:
    day = st.selectbox('Day of week',
        ('Thursday', 'Friday', 'Saturday', 'Sunday'))
    if day == 'Thursday':
        df = df.loc[df['day'] == 'Thur']
    elif day == 'Friday':
        df = df.loc[df['day'] == 'Fri']
    elif day == 'Saturday':
        df = df.loc[df['day'] == 'Sat']
    else:
        df = df.loc[df['day'] == 'Sun']

### Create figures based on user selection and
### display them in 2 columns
st.markdown('---')
st.subheader('\nBill amount distribution')
fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.set_xlabel('Bill ($)')
ax1.set_title('Bill amount distribution')
ax1.hist(df['total_bill'], color='red', alpha=0.5)

fig2 = plt.figure()
ax2 = fig2.add_subplot()
ax2.set_title('Tip amount distribution')
ax2.set_xlabel('Tips (%)')
ax2.hist(df['tip_pct'], color='blue', alpha=0.5)

col1, col2 = st.columns(2)
with col1:
    st.pyplot(fig1)

with col2:
    st.pyplot(fig2)

st.markdown('---')
