from moviepy import VideoFileClip

video_path = "videoplayback.mp4"
audio_path = "match_audio.wav"

print("🚀 Extracting audio...")

video = VideoFileClip(video_path)
video.audio.write_audiofile(audio_path)

print("✅ Audio extracted successfully!")