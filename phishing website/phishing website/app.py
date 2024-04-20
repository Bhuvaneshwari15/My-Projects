from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the dataset
dataset = pd.read_csv('phishing.csv')

# Concatenate relevant columns to create a new 'URL' column
dataset['URL'] = (
    dataset['IpAddress'].astype(str) + '/' +
    dataset['HostnameLength'].astype(str) + '/' +
    dataset['PathLength'].astype(str) + '/'
    # Add other columns as needed
)

# Extract features and labels
X = dataset['URL']
y = dataset['CLASS_LABEL']

# Convert labels to numerical values
le = LabelEncoder()
y_numeric = le.fit_transform(y)

# Convert URLs to TF-IDF vectors
tfidf_vectorizer = TfidfVectorizer()
X_tfidf = tfidf_vectorizer.fit_transform(X)

# Train a Random Forest classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_tfidf, y_numeric)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        url = request.form['url']
        input_data = [url]
        input_tfidf = tfidf_vectorizer.transform(input_data)
        prediction = classifier.predict(input_tfidf)

        return render_template('result.html', url=url, prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
