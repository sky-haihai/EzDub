# README

This project automates the process of converting audio or video files in a specified folder into transcribed text. It identifies the first compatible file, processes it, saves the transcription as a text file, and deletes the original and intermediate files to maintain cleanliness.

## Requirements

To run this script, ensure the following dependencies are installed:

### Python Packages
1. **pydub** - For audio manipulation.
   ```bash
   pip install pydub
   ```
2. **speechrecognition** - For speech-to-text conversion.
   ```bash
   pip install SpeechRecognition
   ```

### Additional Tools
1. **FFmpeg** - Required for `pydub` to handle various audio formats.
   - **Windows**: Download and install from [FFmpeg official site](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **macOS**: Install using Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **Linux**: Install via your package manager:
     ```bash
     sudo apt install ffmpeg
     ```

## Self-Check

Use the following steps to ensure all dependencies are correctly installed:

### Check Python Packages
Run this Python script to check if the required packages are installed:
```python
import importlib.util

# List of required packages
required_packages = ["pydub", "speech_recognition"]

# Check for each package
missing_packages = []
for package in required_packages:
    if importlib.util.find_spec(package) is None:
        missing_packages.append(package)

if missing_packages:
    print(f"Missing packages: {', '.join(missing_packages)}")
else:
    print("All required packages are installed.")
```

### Check FFmpeg Installation
Run the following command in your terminal or command prompt:
```bash
ffmpeg -version
```
If FFmpeg is installed, this will display its version.

## How to Use
1. Place the audio or video file you want to process in the `file` folder.
2. Run the Python script.
   ```bash
   python <script_name>.py
   ```
3. The script will:
   - Locate the first audio or video file in the `file` folder.
   - Convert it to a WAV file (if not already in WAV format).
   - Transcribe the audio to text using Google Speech Recognition.
   - Save the text to a `.txt` file with the same name as the original file.
   - Delete the original file and the intermediate WAV file.

## Supported Formats
- Audio: `.mp3`, `.wav`, `.m4a`, `.aac`
- Video: `.mp4`

## Output
The transcription will be saved in the `file` folder with the same name as the original file but with a `.txt` extension.

## Error Handling
If any errors occur during processing (e.g., file format not supported, network issues with the transcription API), the script will print the error details without deleting the files.

