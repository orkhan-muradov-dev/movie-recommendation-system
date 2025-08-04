import pandas as pd
import re
import nltk
import joblib
import logging
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("preprocess.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logging.info("🚀 Starting preprocessing...")

nltk.download('stopwords')

# Text cleaning
stop_words = set(stopwords.words('english'))

# Load dataset and filter necessary columns
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)

        # Filter the required columns for recommendation
        required_columns = ["genres", "keywords", "overview", "title"]
        df = df[required_columns].dropna().reset_index(drop=True)

        df['combined'] = df['genres'] + ' ' + df['keywords'] + ' ' + df['overview']

        logging.info("🧹 Cleaning text...")
        df['cleaned_text'] = df['combined'].apply(preprocess_text)
        logging.info("✅ Text cleaned.")

        logging.info("✅ Dataset loaded successfully. Total rows: %d", len(df))
        return df
    except FileNotFoundError:
        logging.error("❌ Dataset file not found. Ensure 'movies.csv' is in the correct directory.")
        raise
    except Exception as e:
        logging.error("❌ Failed to load dataset: %s", str(e))
        raise

def preprocess_text(text):
    # Remove special characters and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text).lower()
    # Split text into words and remove stopwords
    words = text.split()
    return " ".join([word for word in words if word not in stop_words])

df = load_data("movies.csv")

# Vectorization
logging.info("🔠 Vectorizing using TF-IDF...")
tfidf = TfidfVectorizer(max_features=5000)
tfidf_matrix = tfidf.fit_transform(df['cleaned_text'])
logging.info("✅ TF-IDF matrix shape: %s", tfidf_matrix.shape)

# Cosine similarity
logging.info("📐 Calculating cosine similarity...")
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
logging.info("✅ Cosine similarity matrix generated.")

# Save processed data
joblib.dump(df, 'df_cleaned.pkl')
joblib.dump(tfidf_matrix, 'tfidf_matrix.pkl')
joblib.dump(cosine_sim, 'cosine_sim.pkl')
logging.info("💾 Data saved to disk.")

logging.info("✅ Preprocessing complete.")