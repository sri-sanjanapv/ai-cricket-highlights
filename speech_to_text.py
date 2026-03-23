import whisper

print("🚀 Loading model...")
model = whisper.load_model("base")  # small + fast

print("🎤 Converting audio to text...")
result = model.transcribe("match_audio.wav")

# Save full text
with open("commentary.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("✅ Text extracted and saved!")

# Show first part
print("\n📢 Sample Commentary:")
print(result["text"][:500])