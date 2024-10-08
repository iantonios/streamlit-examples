# Illustrates use of various input widgets
import streamlit as st

st.subheader('\nRadio buttons')
genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn't select comedy.")

st.markdown('---')
st.subheader('\nSelectbox')
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

st.markdown('---')
st.subheader('\nSlider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
