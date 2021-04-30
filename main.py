import streamlit as st
from multiapp import MultiApp
from apps import home, data, visualization, models
import streamlit.components.v1 as stc

#Title for the page
HTML_BANNER = """
<div style="background-color:#0723f5;padding:10px;border-radius:10px">
<h1 style="color:white;text-align:center;">Coronavirus Sentiment Analysis </h1>
</div>
    """
stc.html(HTML_BANNER)

app = MultiApp()


#Adding all the applications here

app.add_app("Home", home.app)
app.add_app("Dataset", data.app)
app.add_app("Mirror of the Mind", visualization.app)
app.add_app("Models", models.app)

#The main app
app.run()
