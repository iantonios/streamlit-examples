# Illustrates magic commands in Streamlit

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

url = 'https://storage.googleapis.com/scsu-data-science/diabetes_nan.csv'
df = pd.read_csv(url)

# Magic!
df

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(df['Glucose'], df['Insulin'])
ax.set_xlabel('Glucose')
ax.set_ylabel('Insulin')

# More magic
fig
