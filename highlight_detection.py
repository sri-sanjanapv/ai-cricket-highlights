# highlight_detection.py

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

# Split into sentences
sentences = text.split(".")

# Score each sentence
for i, sentence in enumerate(sentences):
    score = 0
    for word in keywords:
        if word in sentence:
            score += keywords[word]

    if score > 0:
        highlights.append((i, score, sentence.strip()))

# Sort by score (highest first)
highlights = sorted(highlights, key=lambda x: x[1], reverse=True)

# Show top highlights
print("\n🔥 TOP HIGHLIGHT MOMENTS:\n")

for h in highlights[:10]:
    print(f"Score: {h[1]} → {h[2]}")