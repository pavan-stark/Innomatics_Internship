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

linkedin = 'https://www.linkedin.com/in/mekapothula-pavan-kalyan-294bb21b5/overlay/contact-info/'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)


st.balloons()
