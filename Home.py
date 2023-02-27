import streamlit as st
import streamlit as st
import pandas as pd
from matplotlib import image
import webbrowser
import os

st.set_page_config(
    page_title="Flipkart Laptop Sales",
)
st.title("Hi,I am Pavan Kalyan")



st.subheader("I am a Data Science Enthusiast \nIntern at Innomatics Research Labs")


Linkedin='https://pavanvis-innomatics-internship-home-wiqze2.streamlit.app/'
if st.button('Linkedin'):
    webbrowser.open_new_tab(Linkedin)


st.balloons()
