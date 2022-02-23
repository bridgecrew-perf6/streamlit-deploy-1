import streamlit as st

headd = st.container()
bodyy = st.container()
taill = st.container()

with headd:
    st.header('Head')

with bodyy:
    st.subheader('Body')

with taill:
    st.text('Tail')

