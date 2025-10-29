import os
import json

TRANSCRIPT_DIR = "audio/transcripts"
os.makedirs(TRANSCRIPT_DIR, exist_ok=True)

transcripts = {
    "conv_001": [
        {"start": 0.00, "end": 3.20, "speaker": "victim", "text": "Hello?"},
        {"start": 3.30, "end": 10.00, "speaker": "scammer", "text": "Sir, main bank fraud department se bol raha hoon. Aapka card block hone wala hai."},
        {"start": 10.10, "end": 18.00, "speaker": "victim", "text": "Ohh, kya karna padega?"},
        {"start": 18.10, "end": 26.00, "speaker": "scammer", "text": "Bas OTP bataye jo abhi aapke phone pe aaya hai."}
    ],
    "conv_002": [
        {"start": 0.00, "end": 4.00, "speaker": "scammer", "text": "Hello, this is the customer care from your bank. We noticed suspicious transactions on your account."},
        {"start": 4.10, "end": 9.00, "speaker": "victim", "text": "Really? What do I need to do?"},
        {"start": 9.10, "end": 15.00, "speaker": "scammer", "text": "Please confirm your card number for verification."},
        {"start": 15.10, "end": 20.00, "speaker": "victim", "text": "Wait, how can I trust this call?"}
    ],
    "conv_003": [
        {"start": 0.00, "end": 3.00, "speaker": "victim", "text": "Hello bhaiya, kaun bol rahe ho?"},
        {"start": 3.10, "end": 9.00, "speaker": "scammer", "text": "Sir main electricity board se bol raha hoon, aapka bill pending hai."},
        {"start": 9.10, "end": 13.50, "speaker": "victim", "text": "Arey maine toh kal hi pay kiya tha."},
        {"start": 13.60, "end": 18.00, "speaker": "scammer", "text": "Nahi sir, system me nahi dikh raha. Aapka connection cut ho sakta hai."}
    ]
}

for conv_id, data in transcripts.items():
    file_path = os.path.join(TRANSCRIPT_DIR, f"{conv_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump({"file_id": conv_id, "segments": data}, f, ensure_ascii=False, indent=2)
    print(f"✅ Transcript saved: {conv_id}.json")

print(" All transcripts generated successfully!")
