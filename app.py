import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit.components.v1 as components

# Display the app name as a title
title_text = "<h1 style='color: #1B9C85;'>Moodify🎧</h1>"
st.markdown(title_text, unsafe_allow_html=True)

# Introduction or tagline
description_text = "<span style='color: #4C4C6D;'>Unleash the Power of Music to Match Your Mood</span>"
st.markdown(f"<h6>{description_text}</h6>", unsafe_allow_html=True)


# Emotion Input
emotion = st.selectbox("Select your current emotion", ["Happy😍", "Sad🥺", "Angry😤", "Relaxed😊"])



# Conditionally show camera input when the checkbox is selected
show_camera = st.button("Take Picture:sunglasses:",use_container_width=True)
if show_camera:
    # Capture the picture
    picture = st.camera_input("")

    if picture:
        st.image(picture)


# Load the dataset into a Pandas DataFrame
df = pd.read_csv("data/dataset.csv")

# Retrieve songs based on genre
desired_genre = "Pop"  # Replace with the desired genre
songs_by_genre = df[df["genre"] == desired_genre]


# Create an empty list to store the song URLs
song_urls = []

# Iterate over the songs in the genre
for index, song in songs_by_genre.iterrows():
    if index<18042:
        # Define the Spotify track URI
        track_uri = song["uri"]

        # Generate the Spotify player embed code
        spotify_player_code = f"""
            <iframe src="https://open.spotify.com/embed/track/{track_uri.split(':')[2]}"
                 width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
            """

        # Add the Spotify player code to the list
        song_urls.append(spotify_player_code)
        

num_cols = 2
num_rows = len(songs_by_genre) // num_cols + 1

# Split the song_urls list into chunks based on the number of columns
chunks = [song_urls[i:i + num_cols] for i in range(0, len(song_urls), num_cols)]

# Display the song previews in a grid
for chunk in chunks:
    col1, col2 = st.columns(num_cols)
    for i, song_preview in enumerate(chunk):
        with col1 if i % num_cols == 0 else col2 if i % num_cols == 1 else col3:
            st.markdown(song_preview, unsafe_allow_html=True)   
