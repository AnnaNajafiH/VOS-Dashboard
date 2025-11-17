import streamlit as st
import pandas as pd
from PIL import Image

# Title
st.title("Voice of Skin Insights")

# Load your CSV data
df = pd.read_csv("results.csv")  # make sure results.csv is in the repo
st.subheader("Summary of Comments")
st.write(df.head())  # or any summary insights

# Display word cloud
img = Image.open("wordcloud.png")  # make sure wordcloud.png is in the repo
st.subheader("Word Cloud of Keywords")
st.image(img)

# Display topic frequency (example)
topic_counts = pd.Series([5, 3, 2], index=["dryness", "maskne", "blue light"])
st.subheader("Topic Frequency")
st.bar_chart(topic_counts)
