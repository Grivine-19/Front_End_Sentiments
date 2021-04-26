import streamlit as st
import time
from apps.data import get_data

covid_data = get_data('data/nrb.csv')

def app():
    st.title("Models")
    
    st.info("Modeling in progress...Come back soon.")

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

