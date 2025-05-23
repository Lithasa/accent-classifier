# 🎤 English Accent Classifier

The Accent Classifier is a Python-based tool that accurately detects and classifies English accents from video URLs. It extracts audio from the given video, processes the speech, and uses a machine learning model to identify the regional accent (e.g., American, British, Australian, etc.).

✅ Features
 - Accepts video URLs as input

 - Extracts and processes audio using moviepy and pydub

 - Converts audio to text and features using speech_recognition, librosa, and transformers

 - Uses a pre-trained model for accurate accent classification

 - Outputs the detected accent with high confidence

🛠️ Requirements
   - Make sure you have Python 3.8+ installed.

✅ Required Packages
Below is the final requirements.txt content:

streamlit                   # For building the web app
moviepy                     # For extracting audio from video
yt-dlp                      # For downloading YouTube and other videos
openai-whisper              # For transcribing speech from audio
torch                       # Backend framework required for Whisper
torchaudio                  # Audio I/O used by Whisper
nest_asyncio                # To allow nested event loops (needed for Streamlit + asyncio)
pytube                      # (optional, not currently used but useful for YouTube video processing)
requests                    # For making HTTP requests (if needed in future)

📦 Setup Instructions
1. Clone the Repository
bash
   git clone https://github.com/your-username/accent-classifier.git
   cd accent-classifier
   
3.  Create a Virtual Environment
python -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

4. Install the Dependencies
   pip install -r requirements.txt
   
5. if pip itself is outdated, update it first:
         python -m pip install --upgrade pip   
    
🎬 Running the App
bash
    streamlit run app.py
The app will open in your default web browser at http://localhost:8501.


✅ Status
This project runs perfectly and has been tested successfully with multiple video URLs. It consistently returns accurate accent classifications, making it suitable for integration with media analytics or language education tools.

⚠️ You must import all the relevant packages before running the script. Missing packages, incompatible package versions will cause errors. 

