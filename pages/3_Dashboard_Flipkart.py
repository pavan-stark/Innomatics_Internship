import pandas as pd
import streamlit as st
import numpy as np
from matplotlib import image

import os

st.title('Flipkart Laptop EDA')

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "flipkart.png")

DATA_PATH = os.path.join(dir_of_interest, "data", "flipkartlaptop.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

data = pd.read_csv(DATA_PATH)
st.dataframe(data)

st.header('Columns of Data Frame')
st.write(data.columns)
st.header('Summary')
st.write(data.describe())

st.header('Prices Of Laptops')
st.bar_chart(data['Price'])

st.header('Types Of Processors')
st.bar_chart(data['Processor_Des'].value_counts())

st.header('Types Of Brand')
st.bar_chart(data['Brand'].value_counts())

st.header('Types Of Processor Brands')
st.bar_chart(data['Processor_Brand'].value_counts())

st.header('Types Of Processor Generations ')
st.bar_chart(data['Processor_Gen'].value_counts())