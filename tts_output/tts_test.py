import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
tts.tts_to_file(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="ko", file_path="output.wav")


tts.tts_to_file(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="ko", file_path="output.wav")