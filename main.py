import streamlit as st
from multiapp import MultiApp
from apps import home, data, visualization, models

app = MultiApp()


#Adding all the applications here

app.add_app("Home", home.app)
app.add_app("Dataset", data.app)
app.add_app("Mirror of the Mind", visualization.app)
app.add_app("Models", models.app)

#The main app
app.run()