import streamlit as st
import pandas as pd
from PIL import Image

# Page config
st.set_page_config(page_title="Voice of Skin Insights", layout="wide", page_icon="💧")

# Header
st.title("💧 Voice of Skin Dashboard")
st.markdown("**Real-time insights from social media about skin care trends**")

# Load data
df = pd.read_csv("results.csv")

# Two-column layout for summary + word cloud
col1, col2 = st.columns(2)

with col1:
    st.subheader("Summary Insights")
    st.write(df.head())  # or your textual summary

with col2:
    st.subheader("Word Cloud of Keywords")
    img_wc = Image.open("wordcloud.png")
    st.image(img_wc, use_column_width=True)

# Tabs for sentiment and topic visualizations
tab1, tab2 = st.tabs(["Sentiment", "Topics"])

with tab1:
    st.subheader("Sentiment Distribution")
    img_sent = Image.open("sentiment.png")
    st.image(img_sent, use_column_width=True)

with tab2:
    st.subheader("Topics Frequency")
    img_topics = Image.open("topics.png")
    st.image(img_topics, use_column_width=True)
