import json

with open("commentary.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

team1 = []
team2 = []

keywords = ["six", "four", "4", "out", "wicket", "bowled", "caught"]

for i, line in enumerate(lines):
    text = line.lower()

    if any(k in text for k in keywords):

        event = {
            "time": i * 5,
            "event": line.strip()
        }

        # 🟢 Split into 2 innings
        if i < len(lines)//2:
            team1.append(event)
        else:
            team2.append(event)

# ⚠️ fallback if low data
def fill_events(events):
    if len(events) < 50:
        for t in range(0, 3600, 40):
            events.append({"time": t, "event": "auto"})
    return events

team1 = fill_events(team1)
team2 = fill_events(team2)

data = {
    "team1": team1[:60],   # ~5 min
    "team2": team2[:60]
}

with open("events.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ events.json ready (Team-wise)")