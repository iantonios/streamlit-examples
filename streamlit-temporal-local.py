# Illustrates use of columns container
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter


filename = 'brooklyn_bridge_pedestrians.csv'
bridge = pd.read_csv(filename,
                     parse_dates=True,
                     index_col='hour_beginning')

st.subheader('Brooklyn Bridge Pedestrian Crossings')
st.markdown('---')
volume = st.radio("Pedestrian Traffic Volume",('Hourly', 'Daily', 'Weekly'))
st.markdown('---')

if volume == 'Hourly':
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot()

    ax.plot(bridge.index, bridge['pedestrians'])
    ax.set_title('Hourly Brooklyn Bridge Pedestrian Traffic, 10/2017-06/2018')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total pedestrians per hour')
    # Define date format
    date_form = DateFormatter('%m-%y')
    ax.xaxis.set_major_formatter(date_form)
    st.pyplot(fig)
elif volume == 'Daily':
    # Extract relevant columns and store in new DataFrame crossings
    crossings = bridge[['pedestrians', 'to_manhattan', 'to_brooklyn']]

    # Resample to weekly interval
    daily = crossings.resample('D').sum()
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot()

    ax.plot(daily.index, daily['to_manhattan'],
            label='Towards Manhattan', linewidth = 3)
    ax.plot(daily.index, daily['to_brooklyn'],
            label='Towards Brooklyn', linewidth = 3)
    ax.set_title('Daily Brooklyn Bridge Pedestrian Traffic, 10/2017-06/2018')
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
    ax.set_title('Weekly Brooklyn Bridge Pedestrian Traffic, 10/2017-06/2018')
    ax.set_xlabel('Date')
    ax.set_ylabel('Total pedestrians per week')

    # Define date format
    date_form = DateFormatter('%m-%y')
    ax.xaxis.set_major_formatter(date_form)
    plt.legend()
    st.pyplot(fig)
