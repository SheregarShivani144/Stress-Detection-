import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

os.makedirs("models", exist_ok=True)

data = {
    "text": [
        "I feel very stressed",
        "I am depressed",
        "I feel anxious",
        "I cannot sleep",
        "I feel relaxed",
        "I am happy",
        "I feel peaceful",
        "I am calm",
        "My work pressure is high",
        "I feel nervous"
    ],
    "label": [2,2,2,2,0,0,0,0,2,2]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
model.fit(X, df["label"])

joblib.dump(model, "models/text_model.joblib")
joblib.dump(vectorizer, "models/vectorizer.joblib")

print("Improved text model saved")
print("Improved text model saved")