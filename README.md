# Jk319-scam_dataset_project-2

# Scam Call Conversation Dataset

##  Overview

This repository contains a structured dataset of **simulated scam-related telephone conversations** designed for:

* Scam detection research
* ASR (Automatic Speech Recognition)
* Speaker diarization experiments
* Real-time fraud prevention models
* Speech-based classification tasks

The dataset includes **Hindi**, **Hinglish**, and **English** conversations with labeled speaker roles: `victim` and `scammer`.

>  **Ethical Notice**: All audio samples included in this dataset are simulated and do *not* involve real victims or fraudulent behavior recorded from the public.

---

##  Dataset Structure

```
scam_dataset_project/
├─ audio/
│  ├─ raw/                # (upload raw real audio here)
│  └─ processed/          # normalized 16kHz WAV
├─ transcripts/           # time-aligned JSON transcripts
├─ diarization/           # speaker segments (JSON)
├─ scripts/               # preprocessing + diarization utilities
├─ metadata.csv           # file-level metadata
├─ README.md
└─ requirements.txt
```


---

## 🧠 Tools Used
| Tool | Purpose |
|------|----------|
| FFmpeg | Audio preprocessing |
| WhisperX | Speech-to-text + timestamps |
| Pyannote.audio | Speaker diarization |
| Python | Data handling, metadata generation |

---

## 🗣️ Language Breakdown
| Language | Count |
|-----------|--------|
| Hindi-English mix | 1 |
| English | 1 |
| Hinglish | 1 |

---

## 💬 Example Transcript
```json
{
  "file_id": "conv_001",
  "duration": 43.2,
  "segments": [
    {"start": 0.00, "end": 1.80, "speaker": "SPEAKER_1", "role": "victim", "text": "Hello?"},
    {"start": 1.81, "end": 7.50, "speaker": "SPEAKER_2", "role": "scammer", "text": "Sir, main bank fraud department se bol raha hoon. Aapka card block hone wala hai."}
  ]
}
```
Dataset Summary
Total Conversations: 7
Total Duration: ~10 minutes
Speakers per call: 2 (scammer, victim)
Type: Simulated (realistic speech)

Languages: Hindi, Hinglish, English

🔗 Links
🎧 Google Drive Folder with Audio Files

💻 GitHub Repository Link

🧾 Citation
If using this dataset for research, please cite:

“Scam Call Speech Dataset (2025).  for AI Research Internship.”
