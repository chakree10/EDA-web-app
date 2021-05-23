import streamlit as st
from multiapp import MultiApp
from apps import home, eda, regressor, classifier # import your app modules here

app = MultiApp()

st.markdown("""
# **Data Science and Machine Learning Pipeline**

**EDA------>Data interpretation------>Model Generation------>Testing**

Designed and built for Research purposes by **CHAKRADAR M** under the guidance of *Dr.Alok Aggarwal*

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data-EDA", eda.app)
app.add_app("Regression-Problem", regressor.app)
app.add_app("Classification-Problem", classifier.app)
# The main app
app.run()
