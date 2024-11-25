import streamlit as st

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
ax.bar(['one', 'two', 'three', 'four', 'five', 'six'],[11, 12, 9, 11, 10, 12])
st.pyplot(fig)


with st.expander("See explanation"):
    st.write('''
        The chart above is generated using the function bar matplotlib.
    ''')
    
