# YouTube MP3 Downloader

A simple Python script to download YouTube videos as MP3 files directly to your Windows Desktop using [yt-dlp](https://github.com/yt-dlp/yt-dlp). FFmpeg must be installed and accessible in your system PATH for audio extraction.

## Features

- Downloads the best audio from a YouTube video
- Converts it to MP3 using FFmpeg
- Saves the file on your Desktop
- Minimal dependencies (Python 3.8+ and yt-dlp)

## Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/download.html) (must be in PATH)

Install yt-dlp via pip:

```bash
pip install yt-dlp
```

## Usage

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the script:

```bash
python downloader.py
```

4. Enter a YouTube URL when prompted.
5. The MP3 file will appear on your Desktop.

## Example

```
Enter YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading audio...
Conversion complete! File saved as "Fake Plastic Trees.mp3" on your Desktop.
```

## Notes

- Ensure FFmpeg is installed and accessible from the command line. You can test this with:

```bash
ffmpeg -version
```

- This script currently supports single video downloads. Playlist downloads can be added in a future version.

## License

This project is licensed under the MIT License.

