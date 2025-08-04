import joblib
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("recommend.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("🔁 Loading data...")
try:
    df = joblib.load('df_cleaned.pkl')
    cosine_sim = joblib.load('cosine_sim.pkl')
    logging.info("✅ Data loaded successfully.")
except FileNotFoundError:
    logging.error("❌ Dataset file not found. Ensure 'movies.csv' is in the correct directory.")
    raise
except Exception as e:
    logging.error("❌ Failed to load required files: %s", str(e))
    raise

# Find top-N similar movies
def recommend_movies(movie_name, top_n=5):
    logging.info("🎬 Recommending movies for: '%s'", movie_name)
    idx = df[df['title'].str.contains(movie_name, case=False)].index
    if len(idx) == 0:
        logging.warning("⚠️ Movie not found in dataset.")
        return None
    idx = idx[0]

    # Get similarity scores and sort them (exclude the movie itself at index 0)
    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:top_n + 1]
    # Extract the indexes of the top similar movies
    movie_indices = [i[0] for i in sim_scores]
    logging.info("✅ Top %d recommendations ready.", top_n)

    return df[['title']].iloc[movie_indices].reset_index(drop=True).to_dict(orient="records")