import openai
import whisper
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt
from transformers import pipeline
import numpy as np
import os
import time

# Initialize Whisper model for speech-to-text
whisper_model = whisper.load_model("base")

# Initialize Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Constants for audio recording
SAMPLE_RATE = 16000  # Sample rate for audio recording
DURATION = 10  # Duration of the recording in seconds

# Feedback log file
FEEDBACK_LOG = "feedback_log.txt"

# Create or open the feedback log
def init_feedback_log():
    if not os.path.exists(FEEDBACK_LOG):
        with open(FEEDBACK_LOG, 'w') as f:
            f.write("Feedback Log\n")
            f.write("------------\n")

def log_feedback(feedback_text, sentiment, score):
    with open(FEEDBACK_LOG, 'a') as f:
        f.write(f"Feedback: {feedback_text}\n")
        f.write(f"Sentiment: {sentiment}, Score: {score}\n")
        f.write("------------\n")

# Record audio
def record_audio():
    print("Recording... Please speak clearly for 10 seconds.")
    try:
        recording = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()  # Wait until recording is finished
        audio_file = "feedback.wav"
        sf.write(audio_file, recording, SAMPLE_RATE)  # Save the audio to a file
        print("Recording complete! Transcribing now...")
        return audio_file
    except Exception as e:
        print(f"Error during audio recording: {e}")
        return None

# Transcribe audio using Whisper
def transcribe_audio(audio_file):
    try:
        result = whisper_model.transcribe(audio_file)
        feedback_text = result["text"]
        print("Transcription:", feedback_text)
        return feedback_text
    except Exception as e:
        print(f"Error during transcription: {e}")
        return None

# Analyze sentiment of the feedback text
def analyze_sentiment(feedback_text):
    try:
        sentiment = sentiment_pipeline(feedback_text)[0]
        print(f"Sentiment: {sentiment['label']}, Score: {sentiment['score']}")
        return sentiment['label'], sentiment['score']
    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
        return None, None

# Visualize sentiment with a bar chart
def visualize_feedback(sentiment, score):
    try:
        labels = ['Positive', 'Negative']
        values = [score if sentiment == 'POSITIVE' else 1 - score, 1 - score if sentiment == 'POSITIVE' else score]

        fig, ax = plt.subplots()
        ax.bar(labels, values, color='green' if sentiment == 'POSITIVE' else 'red')
        ax.set_title(f"Sentiment Analysis: {sentiment}")
        ax.set_ylabel('Confidence Score')
        plt.show()
    except Exception as e:
        print(f"Error during feedback visualization: {e}")

# Main function to tie everything together
def main():
    # Initialize feedback log
    init_feedback_log()

    print("Welcome! Please provide your feedback. This will be recorded for 10 seconds.")

    # Step 1: Record audio
    audio_file = record_audio()
    if audio_file is None:
        print("Audio recording failed. Please try again.")
        return

    # Step 2: Transcribe audio to text
    feedback_text = transcribe_audio(audio_file)
    if feedback_text is None:
        print("Audio transcription failed. Please try again.")
        return

    # Step 3: Perform sentiment analysis
    sentiment, score = analyze_sentiment(feedback_text)
    if sentiment is None:
        print("Sentiment analysis failed. Please try again.")
        return

    # Step 4: Visualize feedback sentiment
    visualize_feedback(sentiment, score)

    # Step 5: Log feedback
    log_feedback(feedback_text, sentiment, score)
    print("Your feedback has been logged. Thank you!")

if __name__ == "__main__":
    main()
