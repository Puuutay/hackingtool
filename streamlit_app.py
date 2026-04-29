import streamlit as st
import os

st.title("HackingTool Web Interface")
st.write("Welcome! Piliin ang option sa ibaba:")

if st.button('Check System'):
    st.success("Gumagana ang Streamlit interface mo!")
    # Halimbawa: ipapakita nito ang laman ng folder
    st.write(os.listdir())
