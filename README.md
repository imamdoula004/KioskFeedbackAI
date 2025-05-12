# Community Feedback System with Sentiment Analysis and Voice Integration

This project is a Community Feedback System that collects feedback from users through a GUI interface and processes it using sentiment analysis and voice integration to help businesses or public services gather insights and improve their services. I made it with the help of ChatGPT, and this can be an amazing implementation for local smart kiosks in public buildings and spaces by the government!  

Features:
Collects Feedback via GUI: Users can input feedback through a graphical interface.

Sentiment Analysis: Uses Hugging Face transformers and OpenAI's models for sentiment analysis to categorize feedback as positive, neutral, or negative.

Voice Feedback Integration: Records voice feedback, converts it to text, and processes the sentiment of the spoken feedback.

Feedback Visualization: Displays a visualization of the feedback sentiment as a chart for easy analysis.

Data Storage: Feedback is stored for further analysis and report generation.

Requirements:
Python 3.11+ (Make sure Python is installed on your PC)

Libraries:

openai

transformers

torch

sounddevice

soundfile

matplotlib

Installation:
1. Install Python 3.11:
Ensure that Python 3.11 (or a compatible version) is installed on your system. You can download it from the official Python website.

2. Set Up Environment:
If you want to use a virtual environment (recommended):

Open Command Prompt (or VSCode terminal).

Navigate to your project directory and create a virtual environment:

bash: 

python -m venv venv


Activate the virtual environment:

Windows:

bash: 

.\venv\Scripts\activate


Mac/Linux:

bash:

source venv/bin/activate



3. Install the Required Libraries:
Use the following command to install all the required libraries for this project:

bash:
pip install openai transformers torch sounddevice soundfile matplotlib

If you face any issues installing sounddevice, follow the steps outlined earlier in the troubleshooting section of the README.



4. Install OpenAI Whisper:
Since we're using OpenAI Whisper for voice-to-text, run the following command:

bash: 
pip install openai-whisper


Running the Code:
Clone the Repository:

Clone this repository to your local machine:

bash: 
git clone https://github.com/your-username/community-feedback-system.git

Replace your-username with your actual GitHub username.

Navigate to the Project Directory:
Go to the directory where the project was cloned:

bash: 

cd community-feedback-system

Run the Python Script:
To run the program, simply execute the following command:

bash: 

python feedback_system.py

How the Program Works:
Graphical User Interface (GUI):

The program will launch a simple GUI where users can input their feedback.

Users will have an option to submit feedback via text or record feedback using their voice.

Voice Feedback:

If the user opts to provide voice feedback, the program will record the speech for 10 seconds, transcribe it into text using OpenAI Whisper, and analyze the sentiment of the text.

Sentiment Analysis:

The feedback text (either typed or spoken) will be processed by Hugging Face transformers and OpenAI's sentiment analysis models to determine if the feedback is positive, neutral, or negative.

Feedback Visualization:

The program will display a visual graph representing the sentiment analysis result.

Results Storage:

All feedback data is stored, and users can view the feedback results and the sentiment score.

Example Usage:
Text Feedback:

Type your feedback in the text box and hit the Submit button. The sentiment analysis result will be displayed.

Voice Feedback:

Press the Record button, speak your feedback for 10 seconds, and the program will transcribe and analyze your voice feedback.

Troubleshooting:
If you get an error related to sounddevice during installation, try installing it using a pre-built .whl file or follow the installation guide here.

Ensure all required libraries are installed using pip.

Contributing:
Feel free to fork this repository, make improvements, and submit pull requests. If you encounter any bugs, please raise an issue on the GitHub repository.
