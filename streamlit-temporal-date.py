# Illustrates use of columns container
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import datetime

# Prevents loading the file every time the user interacts with widgets
@st.cache_data
def load_data():
    URL = 'https://storage.googleapis.com/scsu-data-science/brooklyn_bridge_pedestrians.csv'
    bridge = pd.read_csv(URL,
                         parse_dates=True,
                         index_col='hour_beginning')
    return bridge

bridge = load_data()

st.subheader('Brooklyn Bridge Pedestrian Crossings\n 10/2017-06/2018')
st.markdown('---')
volume = st.radio("Pedestrian Traffic Volume",('Hourly', 'Daily', 'Weekly'))

d_range = st.date_input(
    "Date range",
    value = (datetime.date(2017,10,1), datetime.date(2018,7,1)),
    min_value = datetime.date(2017,10,1),
    max_value = datetime.date(2018,7,1))

st.markdown('---')

if len(d_range) > 1:
    bridge = bridge.loc[d_range[0]:d_range[1], :]
    if volume == 'Hourly':
        fig = plt.figure(figsize=(14, 6))
        ax = fig.add_subplot()

        ax.plot(bridge.index, bridge['pedestrians'])
        ax.set_title('Hourly Brooklyn Bridge Pedestrian Traffic')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total pedestrians per hour')
        # Define date format
        date_form = DateFormatter('%m-%y')
        ax.xaxis.set_major_formatter(date_form)
        st.pyplot(fig)
    elif volume == 'Daily':
        # Extract relevant columns and store in new DataFrame crossings
        crossings = bridge[['pedestrians', 'to_manhattan', 'to_brooklyn']]

        # Resample to daily interval
        daily = crossings.resample('D').sum()
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot()

        ax.plot(daily.index, daily['to_manhattan'],
                label='Towards Manhattan', linewidth = 3)
        ax.plot(daily.index, daily['to_brooklyn'],
                label='Towards Brooklyn', linewidth = 3)
        ax.set_title('Daily Brooklyn Bridge Pedestrian Traffic')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total pedestrians per day')

        # Define date format
        date_form = DateFormatter('%m-%y')
        ax.xaxis.set_major_formatter(date_form)
        plt.legend()
        st.pyplot(fig)
    else:
        # Extract relevant columns and store in new DataFrame crossings
        crossings = bridge[['pedestrians', 'to_manhattan', 'to_brooklyn']]

        # Resample to weekly interval
        weekly = crossings.resample('W').sum()
        fig = plt.figure(figsize=(12, 6))
        ax = fig.add_subplot()

        ax.plot(weekly.index, weekly['to_manhattan'],
                label='Towards Manhattan', linewidth = 3)
        ax.plot(weekly.index, weekly['to_brooklyn'],
                label='Towards Brooklyn', linewidth = 3)
        ax.set_title('Weekly Brooklyn Bridge Pedestrian Traffic')
        ax.set_xlabel('Date')
        ax.set_ylabel('Total pedestrians per week')

        # Define date format
        date_form = DateFormatter('%m-%y')
        ax.xaxis.set_major_formatter(date_form)
        plt.legend()
        st.pyplot(fig)
else:
    st.text('Select end date to generate plot.')
