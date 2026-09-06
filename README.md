# 🎬 8K YT Downloader

A simple YouTube video and audio downloader for Windows.

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

## 📦 Release Files

Each release contains two versions:

### 🟢 `8K-YT-Downloader.exe`

The **ready-to-use Windows version**.

No Python installation is required. Simply download the EXE and run it.

### 🐍 `8K_YT_Downloader.py`

The **Python source code** for the downloader.

The source code is included so users can inspect the program and see exactly how it works.

---

## 💻 Requirements

### For the `.exe`

You need:

* 🪟 Windows
* 🌐 An internet connection
* ⚙️ FFmpeg

**Python and yt-dlp are NOT required.**

### For the `.py` source

You need:

* 🐍 Python
* 🌐 An internet connection
* ⚙️ FFmpeg
* `yt-dlp`
* `Rich`
* `PyFiglet`
* `Pyperclip`

---

## 📥 Using the EXE

No installation is required.

1. Download:

```text
8K-YT-Downloader.exe
```

2. Put it anywhere you like.

3. Double-click the EXE.

4. The downloader will open in a Command Prompt window.

That's it! 🎉

---

## ⚙️ Installing FFmpeg

FFmpeg is required by 8K YT Downloader for combining video and audio streams and converting media formats.

### 1. Download FFmpeg

Download a Windows build of FFmpeg from:

**https://www.gyan.dev/ffmpeg/builds/**

For most users, download the **ffmpeg-release-essentials** ZIP.

### 2. Extract FFmpeg

Extract the downloaded ZIP file.

You can place the extracted folder somewhere simple, such as:

```text
C:\ffmpeg
```

Make sure the following files exist:

```text
C:\ffmpeg\bin\ffmpeg.exe
C:\ffmpeg\bin\ffprobe.exe
```

### 3. Add FFmpeg to PATH

Press:

```text
Windows Key + R
```

Type:

```text
sysdm.cpl
```

and press **Enter**.

Then:

1. Open the **Advanced** tab.
2. Click **Environment Variables**.
3. Under **System variables**, select **Path**.
4. Click **Edit**.
5. Click **New**.
6. Add:

```text
C:\ffmpeg\bin
```

7. Click **OK** on all the windows.

### 4. Check FFmpeg

Close any existing Command Prompt windows and open a new one.

Run:

```text
ffmpeg -version
```

If FFmpeg displays its version information, it is installed correctly. ✅

You can now use **8K YT Downloader**.

---

## ⚡ Quick & Easy Download

Choose:

```text
1) Quick & Easy Download
```

Paste a YouTube URL.

The downloader will automatically download the **highest quality available**.

You can also leave the URL empty if the YouTube link is already copied to your clipboard.

---

## 🛠️ Advanced Download

Choose:

```text
2) Advanced Download
```

Advanced mode lets you choose exactly what you want to download.

### Download Type

```text
1) Audio
2) Video without audio
3) Video + audio
```

---

## 🎥 Video Quality

Available quality options:

```text
1) Best Quality Available
2) 8K
3) 4K
4) 1080p
5) 720p60
6) 480p
7) 360p
8) 240p
9) 144p
```

> The maximum quality depends on what is available for the YouTube video.

---

## 🎞️ Video Formats

Supported video formats:

* **MP4** — Default
* **MKV**
* **WebM**
* **MOV**
* **AVI**

### Recommended

**MP4** is the best choice for general compatibility.

**MKV** can be useful when working with different video/audio streams.

---

## 🎵 Audio Formats

Supported audio formats:

* **MP3**
* **M4A**
* **WAV**
* **FLAC**
* **OPUS**

---

## 📊 Download Progress

The downloader displays live progress while downloading:

```text
╭────────────────────────────────────────────╮
│ Downloading My Video                       │
│                                            │
│ ███████████████████░░░░░░░░░  67.4%        │
│                                            │
│ 8.42 MB/s    1.24 GB / 1.84 GB     00:42  │
╰────────────────────────────────────────────╯
```

For playlists, the current video position is also displayed.

---

## 📚 Playlists

You can download YouTube playlists.

The downloader processes the videos individually and shows the progress of the current video.

---

## 📁 Download Location

Downloads are automatically saved to your Windows **Downloads** folder.

For example:

```text
C:\Users\YourName\Downloads
```

---

## 🔒 Is It a Virus?

**8K YT Downloader is not intended to contain malware, viruses, spyware, or other malicious software.**

The `.exe` is created from the included Python source code using **PyInstaller**.

Because the EXE is a newly built and unsigned Windows executable, some antivirus software or Windows Defender may occasionally display a warning. This can happen with PyInstaller applications, particularly when they are new or have few downloads.

The **Python source code is included with every release** so users can inspect the code themselves.

For safety, only download releases from the official GitHub repository and avoid modified or unofficial copies.

---

## 🚫 Project Usage

**Please do not copy, re-upload, redistribute, or claim this project as your own.**

The source code is provided for transparency and educational purposes.

You may download and use the program, but please **do not create a copy of this project and publish it as your own project**.

If you want to make significant changes or create a separate project based on this code, please contact the original author first.

---

## 🛠️ Built With

* 🐍 **Python**
* 📥 **yt-dlp**
* 🎨 **Rich**
* 🔤 **PyFiglet**
* 📋 **Pyperclip**
* ⚙️ **FFmpeg**
* 📦 **PyInstaller**

---

## ⚖️ Disclaimer

This project is intended for personal and educational use.

Only download content that you have the right or permission to download.

Respect copyright and YouTube's Terms of Service.

---

## ⭐ Support

If you like **8K YT Downloader**, consider giving the repository a ⭐ on GitHub!

Enjoy! 🎬
