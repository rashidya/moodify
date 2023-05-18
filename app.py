import streamlit as st

# Display the app name as a title
title_text = "<h1 style='color: #1B9C85;'>Moodify🎧</h1>"
st.markdown(title_text, unsafe_allow_html=True)

# Introduction or tagline
description_text = "<span style='color: #4C4C6D;'>Unleash the Power of Music to Match Your Mood</span>"
st.markdown(f"<h6>{description_text}</h6>", unsafe_allow_html=True)

# Emotion Input
emotion = st.selectbox("Select your current emotion", ["Happy😍", "Sad🥺", "Angry😤", "Relaxed😊"])

