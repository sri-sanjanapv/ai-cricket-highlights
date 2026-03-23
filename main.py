import cv2

video_path = "videoplayback.mp4"
cap = cv2.VideoCapture(video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_no = 0

timestamps = []

print("🚀 Processing started...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Take 1 frame per second
    if frame_no % fps == 0:
        time_sec = frame_no / fps
        timestamps.append(time_sec)

    # 🔥 SHOW PROGRESS EVERY 1000 FRAMES
    if frame_no % 1000 == 0:
        print(f"Processing frame: {frame_no}")

    frame_no += 1

cap.release()

print("✅ Done!")
print("First 10 timestamps:", timestamps[:10])