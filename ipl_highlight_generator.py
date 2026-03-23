import json
import os

VIDEO = "videoplayback.mp4"
os.makedirs("ipl", exist_ok=True)

with open("events.json") as f:
    data = json.load(f)

clips = []

def create_clips(events, prefix):
    temp = []
    for i, e in enumerate(events):
        start = max(0, e["time"] - 2)
        duration = 5

        out = f"ipl/{prefix}_{i}.mp4"
        temp.append(out)

        cmd = f'ffmpeg -y -ss {start} -i "{VIDEO}" -t {duration} -vf scale=640:360 -c:v libx264 -c:a aac "{out}"'
        os.system(cmd)

    return temp

# 🔥 Team-wise clips
team1_clips = create_clips(data["team1"], "team1")
team2_clips = create_clips(data["team2"], "team2")

# 🟢 Merge in order → Team1 then Team2
all_clips = team1_clips + team2_clips

with open("ipl_list.txt", "w") as f:
    for c in all_clips:
        f.write(f"file '{c}'\n")

os.system('ffmpeg -y -f concat -safe 0 -i ipl_list.txt -c:v libx264 -c:a aac ipl_final.mp4')

print("🏏 FINAL 10 MIN IPL HIGHLIGHT READY")