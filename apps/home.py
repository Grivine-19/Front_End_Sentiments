import streamlit as st
import streamlit.components.v1 as stc

def app():

    #Title for the page
    HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Coronavirus Sentiment Analysis </h1>
    </div>
    """
    stc.html(HTML_BANNER)

    #Layout columns
    #Column_1
    col1, col2 = st.beta_columns([3,2])
    
    with col1:
        options1 = ["About", "Objective", "Tools", "Approach"]
        choice1 = st.selectbox("Navigation", options1)
        if choice1 == "Objective":
            st.subheader("Objective/Scope")
            st.markdown(''' 
            The goal of the project is to analyze the perception of Kenyan's living in 
            Nairobi City on the Coronavirus pandemic for the period February - August 2020.
            ''')
        elif choice1 == "Tools":
            st.subheader("Tools")
            st.markdown(''' 
            Include:
            * Python - Programming Language used for all the tasks outlined in the approach
            * Twitter - Source of data
            * Streamlit - Hosting platform for this Data App
            ''')
        elif choice1 == "Approach":
            st.subheader("Approach/Methodology")
            st.markdown(''' 
            I have adopted sentiment analysis methods that allows me to capture emotions and
            polarity of the sentiments.
            The steps are as follows:
            * Data Scraping
            * Exploratory Data Analysis
            * Sentiment Analysis;

                a. Tokenization

                b. Removal of stop words

                c. Lemmatization

                d. Entity Recognition

                e. Modeling with Bag of Words(BOW)

            * Data App
            ''')
        else:
            st.subheader("About")
            st.markdown(''' 
            This is an analysis of the perception and attitude of Kenyans, in Nairobi,
            on the novel Coronavirus.
            This analysis covers the period February - August 2020.

            Sentiment analysis models focus on polarity (positive, negative, neutral)
            but also on feelings and emotions (angry, happy, sad, etc),
            urgency (urgent,not urgent) and even intentions (interested v. not interested).

            Sentiment analysis algorithms fall into one of three buckets:
            * **Rule-based:** these systems automatically perform sentiment analysis based
            on a set of manually crafted rules.
            * **Automatic:** systems rely on machine learning techniques to learn from data.
            * **Hybrid systems:** combine both rule-based and automatic approaches.

            #### **Created By:**
            #### [Jacklyne Betty](https://www.linkedin.com/in/grivine/ "LinkedIn,Jacklyne") - Professional Mentor
            #### [Grivine Ochieng](https://www.linkedin.com/in/grivine/ "LinkedIn,Grivine") - Data Scientist

            #### **Find the project video here:** *[Youtube](https://bit.ly/2zZCxLb)*

            #### **Acknowledgement:**
            #### *[KamiLimu](https://www.kamilimu.org/)*
            ''')

    #Column_2
    with col2:
        options2 = ["News", "Useful Links"]
        choice2 = st.selectbox("COVID-19 Information", options2)
        if choice2 == "News":
            st.subheader("News")
            st.video("shorturl.at/rAJU5")
            st.video("shorturl.at/gtQT3", start_time=15)
        else:
            st.subheader("Handy Links")
            st.markdown(''' 
            * [Ministry of Health](https://www.health.go.ke/ "MoH Kenya")

            * [World Health Organization](https://covid19.who.int/ "WHO COVID-19 Dashboard")
            ''')
