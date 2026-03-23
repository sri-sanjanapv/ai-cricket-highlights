# highlight_with_time.py

keywords = {
    "six": 5,
    "four": 4,
    "boundary": 3,
    "wicket": 6,
    "out": 5,
    "catch": 4,
    "crowd": 3,
    "cheer": 3,
    "amazing": 2,
    "brilliant": 2
}

highlights = []

# Read commentary
with open("commentary.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

# Split sentences
sentences = text.split(".")

# Assume each sentence ~3 seconds (approximation)
for i, sentence in enumerate(sentences):
    score = 0
    for word in keywords:
        if word in sentence:
            score += keywords[word]

    if score > 0:
        time_sec = i * 3   # ⏱️ estimated timestamp
        highlights.append((time_sec, score, sentence.strip()))

# Sort by score
highlights = sorted(highlights, key=lambda x: x[1], reverse=True)

print("\n🔥 TOP HIGHLIGHTS WITH TIME:\n")

for h in highlights[:10]:
    print(f"Time: {h[0]} sec | Score: {h[1]} → {h[2]}")