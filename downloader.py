import yt_dlp
import os
import shutil
import sys

if shutil.which("ffmpeg") is None:
    print("FFmpeg not found! Please install FFmpeg and add it to your PATH.")
    exit()

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

url = input('Enter YouTube URL: ')
while url:
    # Remove playlist part if present
    url = url.split("&list")[0]
    url = url.split("?list")[0]
    print("Cleaned URL:", url)

    ydl_opts = {
        "format": "bestaudio/best",  # pick best audio
        "postprocessors": [{         # run audio conversion afterwards
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "128",  # optional
        }],
        # "outtmpl": "%(title)s.%(ext)s",  # optional naming
        "outtmpl": os.path.join(desktop, "%(title)s.%(ext)s")
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    url = input('Enter YouTube URL or O to end program: ')
    if url == "0":
        sys.exit(0)
    





