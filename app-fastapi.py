# Load the libraries
import os
from fastapi import FastAPI, HTTPException
from joblib import load

# Load the model
spam_clf = load(open(os.getcwd() + '/notebook/models/spam_detector_model.pkl', 'rb'))

# Load vectorizer
vectorizer = load(open(os.getcwd() + '/notebook/models/vectorizer.pkl', 'rb'))

# Initialize an instance of FastAPI
app = FastAPI()


# Define the default route
@app.get("/")
def root():
    return {"message": "Welcome to Your Sentiment Classification FastAPI"}


# Define the route to the sentiment predictor
@app.post("/predict_sentiment")
def predict_sentiment(text_message):
    polarity = ""
    if not text_message:
        raise HTTPException(
            status_code=400,
            detail="Please Provide a valid text message"
        )

    prediction = spam_clf.predict(vectorizer.transform([text_message]))
    polarity = "Spam" if prediction[0] == 1 else "Ham"

    return {
        "text_message": text_message,
        "sentiment_polarity": polarity
    }