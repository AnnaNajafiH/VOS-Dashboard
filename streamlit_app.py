import streamlit as st
import pandas as pd
from PIL import Image

# --------------------------------------------
# Page Config
# --------------------------------------------

# --------------------------------------------
# Header
# --------------------------------------------
st.title("💧 Voice of Skin – Social Skin Insights Dashboard")
st.markdown(
    """
    ### Understanding consumer conversations through AI  
    This dashboard analyzes real user comments from social media to detect skin concerns, emotions, trending ingredients, and potential product opportunities.
    """
)

# Load data
df = pd.read_csv("results.csv")

# --------------------------------------------
# KPI Cards (3-column layout)
# --------------------------------------------
colA, colB, colC = st.columns(3)

colA.metric("💬 Total Comments", len(df))
colB.metric("🌍 Languages", df["language"].nunique() if "language" in df.columns else "1")
colC.metric("🔥 Topics Detected", df["topic"].nunique() if "topic" in df.columns else "N/A")

st.markdown("---")

# --------------------------------------------
# Summary Section (full width)
# --------------------------------------------
st.subheader("🔍 Summary Insights")
st.info(
    """
    This summary highlights the main concerns, recurring frustrations,  
    and popular ingredients users are discussing across social media.
    """
)

# You can replace df.head() with your actual generated summary string.
if "summary" in df.columns:
    st.write(df["summary"].iloc[0])
else:
    st.write("Summary text placeholder. Insert your generated summary here.")

st.markdown("---")

# --------------------------------------------
# Table Section (full width)
# --------------------------------------------
st.subheader("📊 Sample of Collected Comments")
st.dataframe(df.head(20))

st.markdown("---")

# --------------------------------------------
# Word Cloud (full width)
# --------------------------------------------
st.subheader("☁️ Keyword Word Cloud")
try:
    img_wc = Image.open("wordcloud.png")
    st.image(img_wc, use_column_width=True)
except:
    st.warning("Wordcloud image not found.")

st.markdown("---")

# --------------------------------------------
# Tabs for Sentiment, Topics, Face Impact
# --------------------------------------------
tab1, tab2, tab3 = st.tabs(["💙 Sentiment", "📌 Topics", "🧴 Face Impact Visualizer"])

# ----- Sentiment -----
with tab1:
    st.subheader("💙 Sentiment Distribution")
    try:
        img_sent = Image.open("sentiment.png")
        st.image(img_sent, use_column_width=True)
    except:
        st.warning("sentiment.png not found")

# ----- Topics -----
with tab2:
    st.subheader("📌 Topics Frequency")
    try:
        img_topics = Image.open("topics.png")
        st.image(img_topics, use_column_width=True)
    except:
        st.warning("topics.png not found")

# ----- Face Impact Visualizer -----
with tab3:
    st.subheader("🧴 Product Impact on Skin Zones (Mock Visualization)")
    st.markdown(
        """
        This visual represents how user comments relate to specific skin areas  
        — e.g., dryness on cheeks, irritation near mouth, oiliness on forehead.  
        """
    )

    try:
        img_face = Image.open("face_impact.png")  # Add your face heatmap
        st.image(img_face, use_column_width=True)
    except:
        st.warning("face_impact.png not found — upload heatmap image.")
