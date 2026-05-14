import React from "react";
import "./App.css";

function App() {
  return (
    <div className="main-container">
      <h1>AI Stress Detection</h1>

      <div className="form-card">
        <form action="http://127.0.0.1:5000/detect" method="POST" encType="multipart/form-data">

          <label>Enter Text:</label>

          <textarea
            name="text"
            placeholder="Type your feelings here..."
          ></textarea>

          <label>Upload Voice File (.wav):</label>

          <input
            type="file"
            name="voice"
            accept=".wav"
          />

          <label>Capture Face Image:</label>

          <input
            type="file"
            name="face"
            accept="image/*"
          />

          <button type="submit">
            Detect Stress
          </button>

        </form>
      </div>
    </div>
  );
}
fetch("http://127.0.0.1:5000/detect")
export default App;