import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go 


@st.cache(allow_output_mutation=True)
def get_data(filename):
    covid_data = pd.read_csv(filename)

    return covid_data


def app():
    st.title("The Dataset")

    st.markdown(''' 
    **Source**

    This data was obtained from twitter.
    Scraping of the data was done by Python's Library;Snscrape

    **Timelines**

    The dataset contains tweets between the months of February and August 2020

    **Location**

    The tweets in the dataset are only those posted within Nairobi County and upro a radius
    of 20Km.
    ''')

    st.text("Get a taste of the dataset here")

    covid_data = get_data('data/nrb.csv')

    #Display an interactive  Plotly tabel of the dataset
    fig = go.Figure(data=[go.Table(columnwidth=[2,3,1,1],header=dict(values=list(covid_data[['datetime', 'text',
    'retweets', 'likes']].columns),
    fill_color='#d62728',
    align=['left', 'center'], height=40, font=dict(color='white', size=18)),

    cells=dict(values=[covid_data.datetime, covid_data.text, covid_data.retweets,
    covid_data.likes],
    fill_color='#1f77b4',
    align='left'))
    ])

    fig.update_layout(margin=dict(l=5, r=5, b=10, t=10))
    st.write(fig)

    #Buttons tof data information
    if st.button("Data Info"):
        st.write(covid_data.shape)
        
    
