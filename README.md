# 🎬 Movie Recommendation System



This is a content-based Movie Recommendation System built using Python, Streamlit, and scikit-learn. It recommends similar movies based on genre, keywords, and plot overview using TF-IDF vectorization and cosine similarity.



> ℹ️ **Credits**:  

> This project is **based on a YouTube tutorial** for educational purposes. The core structure and logic follow the tutorial by **[Siddhardhan]** *(https://www.youtube.com/watch?v=Zc4CcUkYKJk&t=205s&ab_channel=Siddhardhan)*. I completed this as part of my coursework and do not claim original authorship of the core algorithm.



---



## 📦 Features



- Preprocess and vectorize movie metadata

- Compute cosine similarity for recommendations

- View results interactively using Streamlit UI

- Fetch additional movie details using OMDB API



---



## 📁 File Structure



```bash
movie-recommendation-system/
├── main.py             /# Streamlit front-end
├── recommend.py        /# Logic for movie recommendation
├── omdb_utils.py       /# OMDB API integration
├── preprocess.py	    /# Text preprocessing + model building
├── requirements.txt
├── README.md
├── .gitignore
├── config.json
└── movies.csv
```

---



## 🔗 Downloads & Setup



### 1. 📥 Download the Dataset



Download movies.csv (approx. 22MB) from the following Google Drive link: https://drive.google.com/file/d/1E6zIdYcILbaZvRE7tB1r29uTY9UtvaU9/view?usp=sharing



Place the file in the root directory of the project.



### 2. 🔑 Add Your API Key



This project uses the [OMDB API](https://www.omdbapi.com/) to fetch additional movie details like plot and poster.



👉 To get your free API key:

1. Visit https://www.omdbapi.com/apikey.aspx

2. Choose the free plan and register with your email

3. You’ll receive an API key via email



Then, put API key to config.json file.



## 🚀 How to Run



### 1. Clone the Repository



```bash

git clone https://github.com/yourusername/movie-recommendation-system.git

cd movie-recommendation-system
```


### 2. Install Dependencies



```bash

pip install -r requirements.txt
```


### 3. Run Preprocessing (only once)



```bash

python preprocess.py
```


### 4. Launch the App



```bash

streamlit run main.py
```
