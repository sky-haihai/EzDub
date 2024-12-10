import os
from pydub import AudioSegment
import speech_recognition as sr

# Define the folder containing audio or video files
folder_path = "file"

# Find the first audio or video file in the folder
file_to_process = None
for file_name in os.listdir(folder_path):
    if file_name.lower().endswith((".mp3", ".wav", ".mp4", ".m4a", ".aac")):
        file_to_process = os.path.join(folder_path, file_name)
        break

if file_to_process:
    # Extract the file name without extension
    base_name = os.path.splitext(os.path.basename(file_to_process))[0]

    # Convert to WAV format if not already in WAV
    if not file_to_process.lower().endswith(".wav"):
        audio = AudioSegment.from_file(file_to_process)
        wav_path = os.path.join(folder_path, f"{base_name}.wav")
        audio.export(wav_path, format="wav")
    else:
        wav_path = file_to_process

    # Transcribe audio to text
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)

        # Save the transcription to a text file
        txt_path = os.path.join(folder_path, f"{base_name}.txt")
        with open(txt_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)

        print(f"Transcription saved to: {txt_path}")

        # Delete the original audio or video file
        os.remove(file_to_process)
        print(f"Deleted original file: {file_to_process}")

        # Delete the WAV file
        if wav_path != file_to_process:
            os.remove(wav_path)
            print(f"Deleted WAV file: {wav_path}")
    except Exception as e:
        print(f"Error processing file: {e}")
else:
    print("No audio or video file found in the folder.")
