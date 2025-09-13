import yt_dlp
import os
import shutil

if shutil.which("ffmpeg") is None:
    print("FFmpeg not found! Please install FFmpeg and add it to your PATH.")
    exit()

desktop = os.path.join(os.path.expanduser("~"), "Desktop")

url = input('Enter YouTube URL: ')

#Case 1
fval = url.rstrip().split('&list')
url = fval[0]
print(url)


#Case 2
fval = url.rstrip().split('?list')
url = fval[0]
print(url)

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



