from flask import Flask, render_template, request
import os
from modules.text_analysis import analyze_text
from modules.face_detection import detect_face_stress
from modules.voice_analysis import detect_voice_stress
from modules.stress_classifier import classify_stress


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/detect", methods=["POST"])
def detect():

    text = request.form.get("text", "")
    voice_file = request.files.get("voice")
    face_file = request.files.get("face")

    text_score = 0
    voice_score = 0
    face_score = 0

    if text.strip():
        text_score = analyze_text(text)

    if voice_file and voice_file.filename != "":
        voice_path = os.path.join(UPLOAD_FOLDER, voice_file.filename)
        voice_file.save(voice_path)
        voice_score = detect_voice_stress(voice_path)

    if face_file and face_file.filename != "":
        face_path = os.path.join(UPLOAD_FOLDER, face_file.filename)
        face_file.save(face_path)
        face_score = detect_face_stress(face_path)

    level, solution = classify_stress(face_score, text_score, voice_score)

    return render_template(
        "result.html",
        level=level,
        solution=solution
    )


if __name__ == "__main__":
    #app.run(debug=True)
    import os

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
