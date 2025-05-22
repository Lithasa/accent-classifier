import nest_asyncio
nest_asyncio.apply()

import asyncio
try:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except Exception:
    pass

import streamlit as st
from utils import download_video_and_extract_audio
from model import classify_accent

# Title and page config
st.set_page_config(page_title="Accent Classifier", page_icon="🎤")
st.title("🎤 English Accent Classifier")
st.write("Upload a public video link (YouTube or direct video file) and detect the speaker's English accent!")

# User input
video_url = st.text_input("📎 Enter Public Video URL (YouTube or direct MP4):")

# Main action
if st.button("🎧 Analyze Accent") and video_url:
    with st.spinner("⏳ Processing video and extracting audio..."):
        audio_path = download_video_and_extract_audio(video_url)

        if not audio_path:
            st.error("❌ Failed to process the video. Please check the URL and try again.")
        else:
            st.success("✅ Audio extracted successfully!")

            with st.spinner("🔍 Classifying accent..."):
                result = classify_accent(audio_path)

                if result:
                    st.markdown(f"### 🎯 Accent Detected: `{result['accent']}`")
                    st.markdown(f"### ✅ English Confidence: `{result['confidence']}%`")
                    st.markdown(f"#### 🧠 Explanation:\n{result['explanation']}")
                else:
                    st.error("❌ Could not classify the accent.")
