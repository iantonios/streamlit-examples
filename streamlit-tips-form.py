import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/tips.csv'
df = pd.read_csv(url)

st.title('Restaurant spending')
# Form ensures that row filtering is applied only after the user
# click submit (Not continuously as they're moving the slider)
with st.form(key='my_form'):
    values = st.slider('Total bill range',
                        0.0, 100.0, (25.0, 75.0))
    submitted = st.form_submit_button(label='Show data and histogram')

    if submitted:
        df = df.loc[((df['total_bill'] > values[0]) & (df['total_bill'] < values[1])), :]
        st.dataframe(df)
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.hist(df['total_bill'])
        ax.set_xlabel('Bill amount')
        st.pyplot(fig)
