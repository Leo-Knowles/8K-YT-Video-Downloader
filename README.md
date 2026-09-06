# 🎬 8K YT Downloader

A simple YouTube video and audio downloader for **Windows and macOS**.

Download videos in up to **8K quality**, extract audio, choose different formats, download playlists, and use clipboard URLs through a clean terminal interface.

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

# 📦 Release Files

Each release contains:

### 🟢 `8K-YT-Downloader.exe`

The **ready-to-use Windows version**.

Python and yt-dlp do **not** need to be installed separately.

### 🐍 `8K_YT_Downloader.py`

The **Python source code**.

This can be run on Windows or macOS if the required dependencies are installed.

The source code is included so users can inspect how the program works.

---

# 🪟 Windows

## 💻 Using the EXE

The easiest way to use 8K YT Downloader on Windows is the `.exe`.

### Requirements

* Windows 10 or newer
* 🌐 Internet connection
* ⚙️ FFmpeg

**Python and yt-dlp are NOT required for the EXE.**

### Installation

No installation is required.

1. Download:

```text
8K-YT-Downloader.exe
```

2. Put it anywhere you like.

3. Double-click the EXE.

4. The downloader will open in a Command Prompt window.

🎉 That's it!

---

# ⚙️ Installing FFmpeg on Windows

FFmpeg is required for combining video and audio streams and converting media formats.

### 1. Download FFmpeg

Download a Windows build from:

[FFmpeg Builds by Gyan.dev](https://www.gyan.dev/ffmpeg/builds/?utm_source=chatgpt.com)

For most users, download the **ffmpeg-release-essentials** ZIP.

### 2. Extract FFmpeg

Extract the downloaded ZIP.

A simple location is:

```text
C:\ffmpeg
```

Make sure these files exist:

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

1. Open **Advanced**.
2. Click **Environment Variables**.
3. Under **System variables**, select **Path**.
4. Click **Edit**.
5. Click **New**.
6. Add:

```text
C:\ffmpeg\bin
```

7. Click **OK** on all windows.

### 4. Check FFmpeg

Open a **new** Command Prompt window and run:

```text
ffmpeg -version
```

If FFmpeg displays its version information, it is installed correctly. ✅

---

# 🍎 macOS

The Windows `.exe` **will not work on macOS**.

However, the included Python version can be run on macOS.

## 🍺 Install using Homebrew

If you don't already have Homebrew installed, install it from:

[Homebrew](https://brew.sh/?utm_source=chatgpt.com)

Then open **Terminal** and install Python and FFmpeg:

```bash
brew install python ffmpeg
```

Install the Python dependencies:

```bash
python3 -m pip install yt-dlp rich pyfiglet pyperclip
```

Navigate to the folder containing:

```text
8K_YT_Downloader.py
```
by typing: cd Downloads (replace Downloads with where you put the .py file)

Then run:

```bash
python3 8K_YT_Downloader.py
```

🎉 The Python version should now run on macOS.

---

# 🐍 Running the Python Version on Windows

You can also run the source code directly on Windows.

### Requirements

* Python
* FFmpeg
* Internet connection

Install the required Python packages:

```bat
py -m pip install yt-dlp rich pyfiglet pyperclip
```

Then run:

```bat
py 8K_YT_Downloader.py
```

---

# ⚡ Quick & Easy Download

Choose:

```text
1) Quick & Easy Download
```

Paste a YouTube URL.

The downloader will automatically download the **highest quality available**.

You can also leave the URL empty if the YouTube link is already copied to your clipboard.

---

# 🛠️ Advanced Download

Choose:

```text
2) Advanced Download
```

Advanced mode lets you choose exactly what you want to download.

## Download Type

```text
1) Audio
2) Video without audio
3) Video + audio
```

---

# 🎥 Video Quality

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

# 🎞️ Video Formats

Supported video formats:

* **MP4** — Default
* **MKV**
* **WebM**
* **MOV**
* **AVI**

### Recommended

**MP4** is recommended for general compatibility.

**MKV** can be useful when working with different video and audio streams.

---

# 🎵 Audio Formats

Supported audio formats:

* **MP3**
* **M4A**
* **WAV**
* **FLAC**
* **OPUS**

---

# 📊 Download Progress

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

# 📚 Playlists

You can download YouTube playlists.

The downloader processes the videos individually and displays the progress of the current video.

---

# 📁 Download Location

Downloads are automatically saved to your system's **Downloads** folder.

On Windows, this is normally:

```text
C:\Users\YourName\Downloads
```

On macOS, this is normally:

```text
/Users/YourName/Downloads
```

---

# 🔒 Is It a Virus?

**8K YT Downloader is not intended to contain malware, viruses, spyware, or other malicious software.**

The Windows `.exe` is created from the included Python source code using **PyInstaller**.

Because the EXE is a newly built and unsigned Windows executable, some antivirus software or Windows Defender may occasionally display a warning. This can happen with PyInstaller applications, particularly when they are new or have few downloads.

The **Python source code is included with every release** so users can inspect the program themselves.

For safety, only download releases from the official GitHub repository and avoid modified or unofficial copies.

---

# 🛠️ Built With

* 🐍 **Python**
* 📥 **yt-dlp**
* 🎨 **Rich**
* 🔤 **PyFiglet**
* 📋 **Pyperclip**
* ⚙️ **FFmpeg**
* 📦 **PyInstaller**

---

# ⚖️ Disclaimer

This project is intended for personal and educational use.

Only download content that you have the right or permission to download.

Respect copyright and YouTube's Terms of Service.

---

# ⭐ Support

If you like **8K YT Downloader**, consider giving the GitHub repository a ⭐!

Enjoy! 🎬
