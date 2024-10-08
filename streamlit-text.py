# Illustrates writing text in Streamlit dashboard
import streamlit as st

st.title('Streamlit is awesome! (st.title)')
st.header('Streamlit is awesome! (st.header)')
st.subheader('Streamlit is awesome! (st.subheader)')
st.text('Streamlit is awesome (st.text)')
st.code("print('code formatting in streamlit using st.code')")

st.markdown('## Markdown')
st.markdown('''
    > This is an example of a blockquote

    Markdown list:
    - apples
    - oranges
    - strawberries

    To learn more about markdown, check out
    [this guide](https://www.markdownguide.org/basic-syntax/)
''')
st.subheader('Equations using Latex')
st.latex(r'''\frac{\sqrt{x^2+1}}{x^{y^2}}''')
