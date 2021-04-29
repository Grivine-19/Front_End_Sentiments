from PIL import Image
from IPython.display import Image
from numpy import column_stack
from numpy.ma import size
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from streamlit.proto.DataFrame_pb2 import Index
from apps.data import get_data
import os
import stylecloud
from stop_words import get_stop_words
import pandas as pd
from collections import Counter
import plotly.figure_factory as ff
from nrclex import NRCLex
import nltk
import spacy 
import operator
from collections import defaultdict

nltk.download('punkt')

covid_data = get_data('data/nrb.csv')

def app():
    st.balloons()
    
    st.markdown("# Visualizations :art:")

    menu = ["Number of Tweets per Day", "Number of Retweets per Day", 
    "Number of Likes per Day", "Most Common Tweets", "Sentiment Scores", "Common Entities"]
    choice = st.selectbox("View", menu)

    if choice == "Number of Retweets per Day":
        fig1 = px.histogram(covid_data, x="datetime", color="retweets", title="Number of Retweets Per Day")
        st.write(fig1)


    elif choice == "Number of Likes per Day":
        fig2 = px.histogram(covid_data, x="datetime", color="likes" ,title="Likes Per Day")
        st.write(fig2)


    elif choice == "Most Common Tweets":
        st.write("Word Cloud for Most Common Tweets")
        stop_words = get_stop_words('english')
        concat_quotes = ' '.join(
            [i for i in covid_data.text_without_stopwords.astype(str)])
        #print(concat_quotes[:10])
        stylecloud.gen_stylecloud(  text=concat_quotes,
                                    icon_name='fab fa-twitter',
                                    palette='cartocolors.qualitative.Bold_9',
                                    background_color='white',
                                    output_name='tweets.png',
                                    collocations=False,
                                    custom_stopwords=stop_words )

        #Displaying image from a file
        Image(filename="tweets.png", width=780, height=780)
        st.image("tweets.png")

        #Display the most common words after stemming
        #
        #Create separate columns
        table_col, input_col = st.beta_columns([3,2])

        covid_data['text_stem'] = covid_data['text_stem'].apply(lambda x:str(x).split()) #Use tokenize or split, smae results
        top = Counter([item for sublist in covid_data['text_stem'] for item in sublist]) #Counts the frequency of words

        with input_col:
            top_n = st.slider("How many of the common words do you want to see?", 0, 5, 10)
            temp = pd.DataFrame(top.most_common(top_n))
            temp.columns = ['common_words', 'count']
            #temp = temp.reset_index()

        with table_col:
            fig = px.pie(temp, values='count', names='common_words',
                         title='Top Common Words',
                         hover_data=['common_words'], color_discrete_sequence=px.colors.qualitative.G10)
            fig.update_layout(showlegend=False, width=450, height=450)
            st.write(fig)
            # colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
            # fig = ff.create_table(temp, height_constant=15, colorscale=colorscale)
            # st.write(fig)
        #st.write(temp.style.background_gradient(cmap = 'Blues'))
        
    elif choice == "Sentiment Scores":
        pie_col, input_col = st.beta_columns([3,2])
       #Convert the text_stem column to string type. nrclext only takes input of type str
        covid_data['text_stem'] = covid_data['text_stem'].astype(str)
        #Create a text object
        text_object = NRCLex(' '.join(covid_data['text_stem']))

        #Create a list from the  text object
        sentiment_scores = pd.DataFrame(list(text_object.raw_emotion_scores.items())) 
        #Create a dataframe of two columns
        sentiment_scores = sentiment_scores.rename(columns={0: "Sentiment", 1: "Count"})
        with input_col:
            num_n = st.slider("Change Pie Chart Values Here", 0, 5, 10)
            sentiment_scores = sentiment_scores.head(num_n)

            btn = st.button("Show Table")
            colorscale = [[0, '#272D31'], [.5, '#ffffff'], [1, '#ffffff']]
            font=['#FCFCFC', '#00EE00', '#008B00']
            if btn:
                fig =  ff.create_table(sentiment_scores, colorscale=colorscale,
                font_colors=font)
                st.write(fig)
        
        with pie_col:
            fig = px.pie(sentiment_scores, values='Count', names='Sentiment',
            title='Top Emotional Affects',
            hover_data=['Sentiment'], color_discrete_sequence=px.colors.qualitative.Dark24)
            fig.update_traces(textposition='inside', textinfo='percent+label')

            fig.update_layout(showlegend = False, width = 450, height = 450,
            font=dict(color='#383635', size=15)
            )

            st.write(fig)

        #Create a dataframe with a dictionary of the sentiments
        st.title("Table Showing Words & Sentiments")

        sentiment_words = pd.DataFrame(list(text_object.affect_dict.items()),columns = ['words','sentiments'])

        num_o = st.slider("Change table size", 0, 50, 100)
        sentiment_words = sentiment_words.head(num_o)
        
        fig = go.Figure(data=[go.Table(columnwidth=[1, 2], header=dict(values=
        list(sentiment_words[['words', 'sentiments']].columns),
            fill_color='maroon',
        align=['left', 'center'], height=40, font=dict(color='white', size=18)),

        cells=dict(values=[sentiment_words.words, sentiment_words.sentiments],
        fill_color='lightseagreen',
        align='left'))
        ])

        fig.update_layout(margin=dict(l=5, r=5, b=10, t=10))
        st.write(fig)

    elif choice == "Common Entities":
        st.write("Word Cloud for Most Common Entities")

        # remove duplicate claims (Not really needed since dropped already)
        words = covid_data.text_stem.unique()
        # NER list we'll use - Perhaps could be expanded?
        nlp = spacy.load('en_core_web_sm')
        corpus = list(nlp.pipe(words[:700]))
        all_ents = defaultdict(int)
        for i, doc in enumerate(corpus):
            #print(i,doc)
            for ent in doc.ents:
                all_ents[str(ent)] += 1
        sorted_ents = pd.DataFrame(sorted(all_ents.items(), key=operator.itemgetter(1), reverse=True),columns = ['entities','count'])

        stop_words = get_stop_words('english')
        hashtags = sorted_ents['entities'].dropna().tolist()
        unique_entities=(" ").join(hashtags)
        # concat_quotes = ' '.join(
        #     [i for i in sorted_ents.entities.astype(str)])
        # #print(concat_quotes[:10])
        stylecloud.gen_stylecloud(  text=unique_entities,
                                    #file_path='concat_quotes',
                                    icon_name='fas fa-comments',
                                    palette='cartocolors.qualitative.Prism_8',
                                    background_color='white',
                                    output_name='entities.png',
                                    collocations=False,
                                    custom_stopwords=stop_words )
        
        #Displaying image from a file
        Image(filename="entities.png", width=780, height=780)
        st.image("entities.png")

    else:
        fig3 = px.histogram(covid_data, x="datetime", title="Number of Tweets Per Day")
        st.write(fig3)


'''#Useful links
makeMappingArray function link = http: // instaar.colorado.edu/~jenkinsc/carboClinic/_carboCELL/Docs/colors.py.htm
'''