import os

video = "videoplayback.mp4"

# Example timestamps from your model (replace with yours)
timestamps = [540, 780, 1020, 1300, 1600, 1900, 2200, 2500]

os.makedirs("highlights", exist_ok=True)

clips = []
total_duration = 0
max_total = 600   # 10 minutes

clip_length = 40  # each clip = 40 sec

for i, t in enumerate(timestamps):
    if total_duration >= max_total:
        break

    start = max(t - 10, 0)
    duration = clip_length

    output = f"highlights/h{i}.mp4"

    cmd = f'ffmpeg -ss {start} -i "{video}" -t {duration} -c copy "{output}" -y'
    os.system(cmd)

    clips.append(output)
    total_duration += duration

# Create file list for merging
with open("file_list.txt", "w") as f:
    for clip in clips:
        f.write(f"file '{clip}'\n")

# Merge all clips
os.system('ffmpeg -f concat -safe 0 -i file_list.txt -c copy final_highlight.mp4 -y')

print("🎬 FINAL 10-MIN HIGHLIGHT READY!")