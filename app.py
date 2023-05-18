import streamlit as st

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


# Featured Songs/Playlists
featured_songs = {
    "Happy": [
        {"title": "Song 1", "artist": "Artist 1"},
        {"title": "Song 2", "artist": "Artist 2"},
        {"title": "Song 3", "artist": "Artist 3"},
        {"title": "Song 4", "artist": "Artist 4"},
        {"title": "Song 5", "artist": "Artist 5"},
    ],
    "Sad": [
        {"title": "Song 6", "artist": "Artist 6"},
        {"title": "Song 7", "artist": "Artist 7"},
        {"title": "Song 8", "artist": "Artist 8"},
        {"title": "Song 9", "artist": "Artist 9"},
        {"title": "Song 10", "artist": "Artist 10"}
    ],
    "Angry": [
        {"title": "Song 11", "artist": "Artist 11"},
        {"title": "Song 12", "artist": "Artist 12"},
        {"title": "Song 13", "artist": "Artist 13"},
        {"title": "Song 14", "artist": "Artist 14"},
        {"title": "Song 15", "artist": "Artist 15"}
    ],
    "Relaxed": [
        {"title": "Song 16", "artist": "Artist 16"},
        {"title": "Song 17", "artist": "Artist 17"},
        {"title": "Song 18", "artist": "Artist 18"},
        {"title": "Song 19", "artist": "Artist 19"},
        {"title": "Song 20", "artist": "Artist 20"}
    ]
}

# Display featured songs for each emotion
for emotion, songs in featured_songs.items():
    st.subheader(emotion)
    # Create a horizontal scroller container
    with st.container():
        # Create columns for song cards
        cols = st.columns(len(songs))
        for col, song in zip(cols, songs):
            with col:
                # Display song card with additional information
                st.image("images/song.jpg", use_column_width=True)
                st.write(f"Title: {song['title']}")
                st.write(f"Artist: {song['artist']}")