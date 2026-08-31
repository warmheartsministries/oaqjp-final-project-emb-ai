"""
This is a Flask server for the Emotion Detector application.
It has endpoints that accepts text and outputs emotions scores.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Retrieves the text to analyze and processes it using the emotion
    detector function. It returns a JSON payload which contains the
    emotions score and the dominant emotion.
    """
    # Retrieve the emotion text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    print(text_to_analyze)

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the emotions is None, indicating an error or invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Try again."
    keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotions_text = emotions_text = ", ".join(f"'{k}': {response[k]}" for k in keys)
    # Return the emotion predictions with the scores
    return(
        f"For the given statement, the system response is {emotions_text}."
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Retrieves the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
