import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from flask import Flask
import mysql.connector

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'moodify-database.c3kt6gsj5iwk.ap-southeast-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'moodify'

# connect mysql database
conn = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)


# Create the login form 
def home(name): 

    st.markdown(f"<h4>Hi {name}</h4>", unsafe_allow_html=True)
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
        if index<18060:
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


# Create the login form 
def login_form(): 
    
    # Initialize session state
    if "button_state" not in st.session_state:
        st.session_state.button_state = {"Sign Up": False}

    # Change the label of Button A based on Button B state
    if st.session_state.button_state["Sign Up"]:
        button_a_label = "Register"
        button_b_label = "Log In"
        msg="Already have an account ?"
    else:
        button_a_label = "Log In"
        button_b_label = "Register"
        msg="Don\'t have an account?"

    # Display the app name as a title
    title_text = "<h1 style='color: #1B9C85; text-align:center;'>Moodify🎧</h1>"
    st.markdown(title_text, unsafe_allow_html=True)

    # Get the username and password from the user 
    username = st.text_input("Username",key="username") 
    password = st.text_input("Password", type='password',key="password") 
 
 
    submit = st.button(button_a_label) 
       

    st.write(msg) 
    if st.button(button_b_label):
         if st.session_state.button_state["Sign Up"] :
            st.session_state.button_state["Sign Up"] = False
         else :
            st.session_state.button_state["Sign Up"] = True
    cursor = conn.cursor() 

    # Check if the login button is clicked 
    if submit: 
        if button_a_label == "Log In":
            query = 'SELECT * FROM user WHERE username=%s AND password=%s' 
            values = (username,password) 
            cursor.execute(query, values) 
            response = cursor.fetchone() 
                # Perform login authentication and user validation here 
                # Replace the condition with your actual login logic 
            if response : 
                    st.success('Logged in successfully!') 
                    st.session_state.page = "home"
                    home(response[1])
            else: 
                    st.error('Invalid credentials') 

        else :
            cursor.execute('INSERT INTO user (username , password ) VALUES (%s, %s)', (username,password))
            conn.commit()
            st.success('Registered successfully!') 

login_form()