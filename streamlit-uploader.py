import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
from io import StringIO
import matplotlib.pyplot as plt

st.title('Histogram plotter')

uploaded_file = st.file_uploader("Choose a file")
# Upload the file after the user makes a selection.
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    # display the dataframe in the app
    st.dataframe(df)

    with st.form(key='my_form'):
        col_name = st.text_input('Input column name:')
        submitted = st.form_submit_button(label='Plot histogram')
        if submitted:
            # Only execute after the user clicks the button.
            # Verify that column name is valid and is numeric before plotting
            if col_name in df.columns and is_numeric_dtype(df[col_name]):
                fig = plt.figure()
                ax = fig.add_subplot()
                ax.hist(df[col_name])
                st.pyplot(fig)
            else:
                st.warning('Column name incorrect or not numeric. Try again.')
