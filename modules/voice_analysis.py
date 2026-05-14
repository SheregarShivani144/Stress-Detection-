import librosa
import numpy as np
import joblib

voice_model = joblib.load("models/voice_model.joblib")

def detect_voice_stress(audio_file):

    audio, sr = librosa.load(audio_file)

    pitch = np.mean(librosa.yin(audio, fmin=50, fmax=300))
    energy = np.mean(np.abs(audio))
    tempo, _ = librosa.beat.beat_track(y=audio, sr=sr)

    features = np.array([[pitch, energy, tempo]])

    prediction = voice_model.predict(features)

    return int(prediction[0])