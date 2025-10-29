import os
from pydub import AudioSegment

RAW_DIR = "audio/raw"
PROCESSED_DIR = "audio/processed"

os.makedirs(PROCESSED_DIR, exist_ok=True)

def process_audio(file_name):
    input_path = os.path.join(RAW_DIR, file_name)
    output_path = os.path.join(PROCESSED_DIR, file_name)

    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_path, format="wav")
    print(f" Processed: {file_name}")

def main():
    for file in os.listdir(RAW_DIR):
        if file.endswith(".wav"):
            process_audio(file)

if __name__ == "__main__":
    main()
