import json
import streamlit as st
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# Load configuration from config.json
try:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
except Exception as e:
    st.error("Error loading configuration: " + str(e))
    st.stop()

OMDB_API_KEY = config.get("OMDB_API_KEY")
if not OMDB_API_KEY:
    st.error("OMDB API key not found in configuration.")
    st.stop()

# Setup the Streamlit page settings
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommender")

# Create a sorted list of movie titles to choose from
movie_list = sorted(df['title'].dropna().unique())
selected_movie = st.selectbox("🎬 Select a movie:", movie_list)

# When the button is clicked, show recommended movies along with details
if st.button("🚀 Recommend Similar Movies"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommend_movies(selected_movie)
        if not recommendations:
            st.warning("Sorry, no recommendations found.")
        else:
            st.success("Top similar movies:")
            for movie in recommendations:
                movie_title = movie['title']
                plot, poster = get_movie_details(movie_title, OMDB_API_KEY)
                # Create two columns: one for the poster and one for the details
                col1, col2 = st.columns([1, 3])
                with col1:
                    if poster != "N/A":
                        st.image(poster, width=100)
                    else:
                        st.write("❌ No Poster Found")
                with col2:
                    st.markdown(f"### {movie_title}")
                    st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")