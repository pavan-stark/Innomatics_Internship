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

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR,os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR,"proj_1")

IMAGE_PATH = os.path.join(dir_of_interest,"pavan","photo.png")

img = image.imread(IMAGE_PATH)
st.image(img)

st.subheader("I am a Data Science Enthusiast \nIntern at Innomatics Research Labs")

linkedin = 'https://www.linkedin.com/in/mekapothula-pavan-kalyan-294bb21b5/overlay/contact-info/'

if st.button('Linkedin'):
    webbrowser.open_new_tab(linkedin)


st.balloons()
