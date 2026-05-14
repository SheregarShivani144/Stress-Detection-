import joblib

model = joblib.load("models/text_model.joblib")
vectorizer = joblib.load("models/vectorizer.joblib")

def analyze_text(text):

    X = vectorizer.transform([text])

    prediction = model.predict(X)

    return int(prediction[0])