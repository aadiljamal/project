import streamlit as st
import webbrowser

st.write("try link")

url = 'https://www.streamlit.io/'
link = '[GitHub](http://github.com)'
st.markdown(link, unsafe_allow_html=True)

if st.button('Open painting tool'):
    webbrowser.open_new_tab(url)