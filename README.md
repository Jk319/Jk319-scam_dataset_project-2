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

##  Audio Format

All processed audio files follow:

* **WAV** format
* **16kHz sample rate**
* **Mono channel**
* Normalized amplitude

Raw recordings can be any format (MP3/M4A/WAV) — use `preprocess.py` to convert.

---

##  Speaker Roles

Each transcript segment includes:

* Time start (seconds)
* Time end (seconds)
* Speaker ID
* Participant role (victim/scammer)
* Content text

### Example

```json
{
  "start": 1.21,
  "end": 3.90,
  "speaker": "SPEAKER_2",
  "role": "scammer",
  "text": "This is bank fraud department, we detected suspicious activity."
}
```

---

##  Time-Aligned Transcripts

Located in:

```
transcripts/*.json
```

Each file corresponds to a single conversation.

---

##  Diarization Files

Located in:

```
diarization/*.json
```

They contain segment-level speaker boundaries.

---

##  Metadata

Open `metadata.csv` to view:

* file_id
* duration_sec
* num_speakers
* speaker_roles
* source_type (simulated/public)
* recording conditions
* notes

This file enables indexing or research automation.

---

##  Installation

```bash
pip install -r requirements.txt
```

### Additional Dependencies

* **ffmpeg** required for audio transcoding

Install via:

```bash
sudo apt install ffmpeg
```

---

##  Usage

### 1. Normalize + Convert Audio

```bash
python scripts/preprocess.py
```

### 2. Run Diarization (pyannote)

Update `diarize_transcribe.py` with your HuggingFace token, then:

```bash
python scripts/diarize_transcribe.py
```

### 3. View Transcript JSON

Open any file:

```
transcripts/conv_001.json
```

---

##  Download Raw Audio (Google Drive)

Raw audio files (if large) will be available here:



---

##  Dataset Summary

* **Total Conversations**: 3 (expandable)
* **Languages**: Hindi, Hinglish, English
* **Speakers**: 2 per call
* **Avg Duration**: 4–6 seconds (placeholder, replace when real audio added)
* **Source**: Simulated scam calls created ethically

> You may add additional realistic conversations by recording consenting participants.

---

##  Ethics & Compliance

This dataset:

* Does **not** contain personal/private information
* Does **not** record real victims
* Is used strictly for **research**, **education**, and **cybersecurity awareness**
* Complies with privacy norms

Any real recordings must be:

* Consent recorded
* Anonymized (no names, card details, phone numbers)

---

##  Research Applications

This dataset can be used for:

* Scam detection models
* Language modeling
* Fraud intent classification
* Speaker change detection
* Phishing call analysis

---

##  Tools Used

Recommended stack:

* OpenAI Whisper (ASR)
* Pyannote (Diarization)
* Pydub + FFmpeg (Preprocessing)
* Torch (Inference GPU)

---

##  Contributing

Pull requests welcome for:

* Additional languages
* Longer conversations
* Noisy environment samples
* Edge-case scenarios

---

##  License

```
Research/Educational Only — Not for commercial fraud or data harvesting.
Misuse strictly prohibited.
```

---


###  If Used in Research

Please cite the GitHub repository link.

