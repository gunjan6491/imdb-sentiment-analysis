# 🎬 IMDb Movie Review Sentiment Analysis

A Machine Learning web application that predicts whether a movie review expresses a **Positive** or **Negative** sentiment using Natural Language Processing (NLP).

# Project Overview

This project uses the IMDb Movie Reviews dataset to build a sentiment classification model. Users can enter a movie review on the website and get an instant sentiment prediction.

# Features

- Predicts positive and negative movie reviews.
- Text preprocessing using NLP techniques.
- TF-IDF for text feature extraction.
- Naive Bayes classification model.
- Interactive web interface built with Flask.
- Real-time sentiment prediction.

 # Technologies Used

- Python
- Pandas & NumPy
- NLTK
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Flask
- HTML, CSS & JavaScript
- Git & GitHub

# Machine Learning Workflow

1. Dataset collection and exploration.
2. Data cleaning and preprocessing.
3. Text normalization and lemmatization.
4. Feature extraction using TF-IDF.
5. Model training using Multinomial Naive Bayes.
6. Model evaluation.
7. Deployment using Flask.

 # Project Structure
 
imdb-sentiment-analysis/
│
├── app.py
├── preprocessing.py
├── naive_bayes.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js

# Installation & Setup

1. # Clone the repository

bash
git clone https://github.com/gunjan6491/imdb-sentiment-analysis.git

2. # Navigate to the project folder
bash
cd imdb-sentiment-analysis

3. # Install dependencies

bash
pip install -r requirements.txt

4. # Run the Flask application
`bash
python app.py

# Dataset

The project uses the IMDb 50K Movie Reviews dataset containing movie reviews labelled as Positive or Negative.

# Future Improvements

- Improve model performance.
- Add more machine learning models.
- Display prediction confidence.
- Improve website UI and user experience.

# Author
Gunjan Aswani

B.Tech – Artificial Intelligence & Machine Learning

⭐ If you find this project interesting, feel free to star the repository!
