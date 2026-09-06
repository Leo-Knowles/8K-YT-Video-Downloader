# 🎬 8K YT Downloader

A simple YouTube video and audio downloader built with Python and `yt-dlp`.

Download videos in up to **8K quality**, extract audio, choose different formats, and download playlists through a clean terminal interface.

---

## ✨ Features

* 🚀 Download videos up to **8K**
* 🎥 Video + audio downloads
* 🎞️ Video-only downloads
* 🎵 Audio-only downloads
* 📚 Playlist support
* 📋 Clipboard URL support
* 📊 Live download progress
* ⚡ Quick & Easy download mode
* 🛠️ Advanced download mode
* 🎬 Multiple video formats
* 🎧 Multiple audio formats
* 🔵 Clean blue terminal interface
* 💾 Automatically saves downloads to your Downloads folder

---

## 🎥 Video Quality

Choose from:

* Best Quality Available
* 8K
* 4K
* 1080p
* 720p60
* 480p
* 360p
* 240p
* 144p

> The maximum quality depends on what is available for the video.

---

## 🎞️ Video Formats

Supported formats:

* **MP4** — Default and most compatible
* **MKV**
* **WebM**
* **MOV**
* **AVI**

---

## 🎵 Audio Formats

Supported audio formats:

* **MP3**
* **M4A**
* **WAV**
* **FLAC**
* **OPUS**

---

## 📥 Installation

### 1. Download the file

Download **`8K-YT-Downloader.py`** from this GitHub repository.

### 2. Open the downloaded file's folder

For example, if you downloaded it to your **Downloads** folder, open:

```text
Your Downloads Folder
```

### 3. Open Command Prompt in that folder

Click the address bar at the top of File Explorer where it says:

```text
Downloads
```

Type:

```text
cmd
```

Then press **Enter**.

### 4. Start the downloader

In the Command Prompt window, type:

```text
py 8K-YT-Downloader.py
```

Then press **Enter**.

That's it! 🎉

(Sometimes You Can Just Right Click on the file then select open with then click python)
---

## ⚡ Quick & Easy

Choose:

```text
1) Quick & Easy Download
```

Paste your YouTube URL and the downloader will automatically use the highest quality available.

You can also leave the URL empty if the YouTube link is already copied to your clipboard.

---

## 🛠️ Advanced Download

Advanced mode gives you more control.

### Download Type

```text
1) Audio
2) Video without audio
3) Video + audio
```

You can then select your preferred quality and format.

---

## 📊 Download Progress

The downloader displays a live progress bar while downloading:

```text
╭────────────────────────────────────────────╮
│ Downloading My Video                       │
│                                            │
│ ███████████████████░░░░░░░░░  67.4%        │
│                                            │
│ 8.42 MB/s    1.24 GB / 1.84 GB     00:42  │
╰────────────────────────────────────────────╯
```

For playlists, the current video number is also shown.

---

## 📁 Download Location

Downloads are automatically saved to your Windows **Downloads** folder:

```text
C:\Users\YourName\Downloads
```

---

## 🔧 Requirements

You need:

* Windows
* Python
* FFmpeg
* An internet connection

The downloader uses:

* `yt-dlp`
* `FFmpeg`
* `Rich`
* `PyFiglet`
* `Pyperclip`

---

## ⚠️ Troubleshooting

### `py` is not recognised

Make sure Python is installed and added to your PATH.

You can test it with:

```text
py --version
```

### yt-dlp errors

Try updating yt-dlp:

```text
py -m pip install -U yt-dlp
```

### FFmpeg errors

Make sure FFmpeg is installed and available from Command Prompt:

```text
ffmpeg -version
```

---

## ⚖️ Disclaimer

This project is intended for personal and educational use.

Only download content that you have the right or permission to download. Respect copyright and YouTube's Terms of Service.

---

## ⭐ Support

If you like **8K YT Downloader**, consider giving the repository a ⭐ on GitHub!

Enjoy! 🎬
