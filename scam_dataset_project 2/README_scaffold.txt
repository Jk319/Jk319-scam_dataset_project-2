scam_dataset_project - scaffold
This folder contains placeholder/example dataset files and scripts for creating a scam-call dataset.
Files created:
- audio/processed/*.wav  (placeholder WAVs)
- transcripts/*.json
- diarization/*_diarization.json
- metadata.csv
- scripts/ (template scripts and requirements.txt)

Next steps:
1. Replace placeholder WAVs with real or synthesized audio (ensure legal/ethical sourcing).
2. Run preprocess.py to normalize audio.
3. Use diarize_transcribe.py as a template to run pyannote and Whisper and produce final JSON transcripts/diarization.

Note: This is a delivered scaffold. To generate a full dataset and run heavy models, run the scripts on a machine with ffmpeg and required Python packages installed.
