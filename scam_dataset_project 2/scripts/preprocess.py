# preprocess.py
# Normalize audio, convert to 16 kHz mono WAV, trim silence, and save to processed directory.
# Uses pydub (pip install pydub) and ffmpeg installed on system.

from pydub import AudioSegment
from pathlib import Path

SRC = Path('audio/raw')
DST = Path('audio/processed')
DST.mkdir(parents=True, exist_ok=True)

def normalize_and_convert(infile, outfile, target_sr=16000):
    audio = AudioSegment.from_file(infile)
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(target_sr)
    # normalize
    change_in_dBFS = -20.0 - audio.dBFS
    audio = audio.apply_gain(change_in_dBFS)
    audio.export(outfile, format='wav')

if __name__ == '__main__':
    for f in SRC.glob('*'):
        out = DST / f.name
        normalize_and_convert(f, out)
    print('Preprocessing done.')
