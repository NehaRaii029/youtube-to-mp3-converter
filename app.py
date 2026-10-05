import yt_dlp
import os

url = input("Enter YouTube URL: ")

os.makedirs("downloads", exist_ok=True)

options = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(title)s.%(ext)s",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

try:
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    print("\nMP3 downloaded successfully!")

except Exception as e:
    print("\nDownload failed:")
    print(e)