import matplotlib.pyplot as plt
import mpld3
import streamlit.components.v1 as components

# Need to install mpld3
# At a terminal window type:
#      pip3 install mpld3  (or pip install mpld3)

# create your figure and get the figure object returned
fig = plt.figure()
ax = fig.add_subplot()
ax.plot([1, 2, 3, 4, 5])
ax.set_xlabel('x axis')

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
