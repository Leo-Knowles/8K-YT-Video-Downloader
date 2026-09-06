import os
import re
import shutil
import pyperclip
import pyfiglet
import yt_dlp

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live


# ============================================================
# 8K YT DOWNLOADER
# ============================================================

console = Console()

BLUE = "#0088ff"
LIGHT_BLUE = "#33aaff"

DOWNLOAD_FOLDER = os.path.join(
    os.path.expanduser("~"),
    "Downloads"
)


# ============================================================
# SCREEN
# ============================================================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ============================================================
# BLUE TEXT
# ============================================================

def blue_text(text, bright=False):
    return Text(
        str(text),
        style=LIGHT_BLUE if bright else BLUE
    )


def bprint(text="", bright=False):
    console.print(
        blue_text(text, bright)
    )


def binput(prompt):
    console.print(
        blue_text(prompt, bright=True),
        end=""
    )

    value = input().strip()

    return value


# ============================================================
# BANNER
# ============================================================

def banner():
    clear_screen()

    title = pyfiglet.figlet_format(
        "8K YT",
        font="big"
    )

    subtitle = pyfiglet.figlet_format(
        "DOWNLOADER",
        font="big"
    )

    console.print(
        blue_text(title, bright=True),
        end=""
    )

    console.print(
        blue_text(subtitle, bright=True),
        end=""
    )

    console.print()

    console.print(
        Panel.fit(
            blue_text(
                "YouTube Video & Audio Downloader",
                bright=True
            ),
            border_style=BLUE
        )
    )

    console.print()


# ============================================================
# URL
# ============================================================

def get_url():
    bprint(
        "Paste a YouTube URL below.",
        bright=True
    )

    bprint(
        "Leave it empty to use your clipboard.\n"
    )

    url = binput(
        "URL: "
    )

    if not url:
        try:
            url = pyperclip.paste().strip()
        except Exception:
            url = ""

        if url:
            bprint(
                "\nURL loaded from clipboard.",
                bright=True
            )

    if not url:
        bprint(
            "\nNo URL entered."
        )
        return None

    if not re.search(
        r"(youtube\.com|youtu\.be)",
        url,
        re.IGNORECASE
    ):
        bprint(
            "\nThat doesn't look like a YouTube URL."
        )
        return None

    return url


# ============================================================
# QUALITY OPTIONS
# ============================================================

QUALITY_MAP = {
    "1": (
        "Best Quality Available",
        "bestvideo+bestaudio/best"
    ),

    "2": (
        "8K",
        "bestvideo[height<=4320]+bestaudio/best"
    ),

    "3": (
        "4K",
        "bestvideo[height<=2160]+bestaudio/best"
    ),

    "4": (
        "1080p",
        "bestvideo[height<=1080]+bestaudio/best"
    ),

    "5": (
        "720p60",
        "bestvideo[height<=720][fps<=60]+bestaudio/best"
    ),

    "6": (
        "480p",
        "bestvideo[height<=480]+bestaudio/best"
    ),

    "7": (
        "360p",
        "bestvideo[height<=360]+bestaudio/best"
    ),

    "8": (
        "240p",
        "bestvideo[height<=240]+bestaudio/best"
    ),

    "9": (
        "144p",
        "bestvideo[height<=144]+bestaudio/best"
    )
}


# ============================================================
# VIDEO FORMATS
# ============================================================

VIDEO_FORMATS = {
    "1": ("MP4", "mp4"),
    "2": ("MKV", "mkv"),
    "3": ("WebM", "webm"),
    "4": ("MOV", "mov"),
    "5": ("AVI", "avi")
}


# ============================================================
# AUDIO FORMATS
# ============================================================

AUDIO_FORMATS = {
    "1": ("MP3", "mp3"),
    "2": ("M4A", "m4a"),
    "3": ("WAV", "wav"),
    "4": ("FLAC", "flac"),
    "5": ("OPUS", "opus")
}


# ============================================================
# QUALITY MENU
# ============================================================

def choose_quality():

    bprint(
        "\nVIDEO QUALITY",
        bright=True
    )

    bprint(
        "────────────────────────"
    )

    for key, value in QUALITY_MAP.items():

        label = value[0]

        if key == "1":
            label += " (Recommended)"

        bprint(
            f"{key}) {label}"
        )

    bprint()

    choice = binput(
        "Choose quality: "
    )

    if choice not in QUALITY_MAP:
        choice = "1"

    return QUALITY_MAP[choice]


# ============================================================
# VIDEO FORMAT MENU
# ============================================================

def choose_video_format():

    bprint(
        "\nVIDEO FORMAT",
        bright=True
    )

    bprint(
        "────────────────────────"
    )

    for key, value in VIDEO_FORMATS.items():

        label = value[0]

        if key == "1":
            label += " (Default)"

        if key == "2":
            label += " (Recommended for compatibility with streams)"

        bprint(
            f"{key}) {label}"
        )

    bprint()

    choice = binput(
        "Choose format: "
    )

    if choice not in VIDEO_FORMATS:
        choice = "1"

    return VIDEO_FORMATS[choice]


# ============================================================
# AUDIO FORMAT MENU
# ============================================================

def choose_audio_format():

    bprint(
        "\nAUDIO FORMAT",
        bright=True
    )

    bprint(
        "────────────────────────"
    )

    for key, value in AUDIO_FORMATS.items():

        label = value[0]

        if key == "1":
            label += " (Default)"

        bprint(
            f"{key}) {label}"
        )

    bprint()

    choice = binput(
        "Choose format: "
    )

    if choice not in AUDIO_FORMATS:
        choice = "1"

    return AUDIO_FORMATS[choice]


# ============================================================
# FORMAT BYTES
# ============================================================

def format_bytes(value):

    if value is None:
        return "0 B"

    try:
        value = float(value)
    except Exception:
        return "0 B"

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB"
    ]

    for unit in units:

        if value < 1024:
            return f"{value:.2f} {unit}"

        value /= 1024

    return f"{value:.2f} PB"


# ============================================================
# FORMAT TIME
# ============================================================

def format_time(seconds):

    if seconds is None:
        return "--:--"

    try:
        seconds = int(seconds)
    except Exception:
        return "--:--"

    hours, remainder = divmod(
        seconds,
        3600
    )

    minutes, seconds = divmod(
        remainder,
        60
    )

    if hours:
        return (
            f"{hours:02d}:"
            f"{minutes:02d}:"
            f"{seconds:02d}"
        )

    return (
        f"{minutes:02d}:"
        f"{seconds:02d}"
    )


# ============================================================
# SPEED
# ============================================================

def format_speed(speed):

    if not speed:
        return "0 B/s"

    return (
        f"{format_bytes(speed)}/s"
    )


# ============================================================
# PROGRESS BAR
# ============================================================

def make_bar(
    percent,
    width=32
):

    percent = max(
        0,
        min(
            100,
            percent
        )
    )

    filled = int(
        width * percent / 100
    )

    empty = width - filled

    return (
        "█" * filled +
        "░" * empty
    )


# ============================================================
# PROGRESS
# ============================================================

class DownloadProgress:

    def __init__(
        self,
        title,
        playlist_index=None,
        playlist_total=None
    ):

        self.title = title

        self.playlist_index = (
            playlist_index
        )

        self.playlist_total = (
            playlist_total
        )

        self.percent = 0
        self.downloaded = 0
        self.total = 0
        self.speed = 0
        self.eta = None

    def update(self, data):

        if data.get("status") != "downloading":
            return

        downloaded = (
            data.get("downloaded_bytes")
            or 0
        )

        total = (
            data.get("total_bytes")
            or data.get("total_bytes_estimate")
            or 0
        )

        self.downloaded = downloaded
        self.total = total

        if total:
            self.percent = (
                downloaded /
                total
            ) * 100

        self.speed = (
            data.get("speed")
            or 0
        )

        self.eta = data.get(
            "eta"
        )

    def render(self):

        title = self.title

        if (
            self.playlist_index is not None
            and self.playlist_total is not None
        ):

            title += (
                f" "
                f"({self.playlist_index}/"
                f"{self.playlist_total})"
            )

        bar = make_bar(
            self.percent
        )

        line1 = (
            f"Downloading {title}"
        )

        line2 = (
            f"{bar} "
            f"{self.percent:5.1f}%"
        )

        if self.total:

            size_text = (
                f"{format_bytes(self.downloaded)}"
                f" / "
                f"{format_bytes(self.total)}"
            )

        else:

            size_text = (
                format_bytes(
                    self.downloaded
                )
            )

        line3 = (
            f"{format_speed(self.speed):<14}"
            f"{size_text:<25}"
            f"{format_time(self.eta)}"
        )

        text = Text()

        text.append(
            line1 + "\n\n",
            style=LIGHT_BLUE
        )

        text.append(
            line2 + "\n\n",
            style=BLUE
        )

        text.append(
            line3,
            style=BLUE
        )

        return Panel(
            text,
            border_style=BLUE,
            padding=(0, 1)
        )


# ============================================================
# FFMPEG CHECK
# ============================================================

def check_ffmpeg():

    if shutil.which("ffmpeg") is None:
        return False

    if shutil.which("ffprobe") is None:
        return False

    return True


# ============================================================
# DOWNLOAD
# ============================================================

def download(
    url,
    fmt,
    audio_only=False,
    container="mp4"
):

    os.makedirs(
        DOWNLOAD_FOLDER,
        exist_ok=True
    )

    # --------------------------------------------------------
    # FFMPEG
    # --------------------------------------------------------

    if not check_ffmpeg():

        bprint(
            "\nDOWNLOAD FAILED",
            bright=True
        )

        bprint(
            "FFmpeg or FFprobe could not be found."
        )

        bprint(
            "Make sure C:\\ffmpeg\\bin is on PATH."
        )

        return False

    # --------------------------------------------------------
    # GET INFO
    # --------------------------------------------------------

    info_options = {
        "quiet": True,
        "no_warnings": True
    }

    try:

        with yt_dlp.YoutubeDL(
            info_options
        ) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )

    except Exception as error:

        bprint(
            "\nDOWNLOAD FAILED",
            bright=True
        )

        bprint(
            str(error)
        )

        return False

    # --------------------------------------------------------
    # PLAYLIST
    # --------------------------------------------------------

    entries = info.get(
        "entries"
    )

    if entries:

        entries = [
            entry
            for entry in entries
            if entry
        ]

        playlist_total = len(
            entries
        )

    else:

        entries = [info]

        playlist_total = 1

    # --------------------------------------------------------
    # BASE OPTIONS
    # --------------------------------------------------------

    options = {

        "outtmpl": os.path.join(
            DOWNLOAD_FOLDER,
            "%(title)s.%(ext)s"
        ),

        "windowsfilenames": True,

        "quiet": True,

        "no_warnings": True,

        "retries": 10,

        "fragment_retries": 10,

        "concurrent_fragment_downloads": 4,

        "continuedl": True,

        "overwrites": False,

        "noplaylist": True
    }

    # --------------------------------------------------------
    # AUDIO
    # --------------------------------------------------------

    if audio_only:

        options["format"] = (
            "bestaudio/best"
        )

        options["postprocessors"] = [

            {
                "key": "FFmpegExtractAudio",

                "preferredcodec": container,

                "preferredquality": "320"
            }

        ]

    # --------------------------------------------------------
    # VIDEO
    # --------------------------------------------------------

    else:

        options["format"] = fmt

        options[
            "merge_output_format"
        ] = container

    # --------------------------------------------------------
    # DOWNLOAD
    # --------------------------------------------------------

    successful = True

    for index, entry in enumerate(
        entries,
        start=1
    ):

        title = (
            entry.get("title")
            or "Unknown"
        )

        video_url = (
            entry.get("webpage_url")
            or entry.get("original_url")
            or url
        )

        progress = DownloadProgress(

            title,

            playlist_index=(
                index
                if playlist_total > 1
                else None
            ),

            playlist_total=(
                playlist_total
                if playlist_total > 1
                else None
            )
        )

        # ----------------------------------------------------
        # SINGLE LIVE DISPLAY
        # ----------------------------------------------------

        def progress_hook(data):

            progress.update(
                data
            )

            live.update(
                progress.render()
            )

        options[
            "progress_hooks"
        ] = [
            progress_hook
        ]

        try:

            with Live(
                progress.render(),

                console=console,

                refresh_per_second=10,

                transient=True,

                screen=False
            ) as live:

                with yt_dlp.YoutubeDL(
                    options
                ) as ydl:

                    ydl.download(
                        [video_url]
                    )

        except Exception as error:

            successful = False

            bprint(
                "\nDOWNLOAD FAILED",
                bright=True
            )

            bprint(
                str(error)
            )

            continue

        bprint(
            f"\nFinished: {title}",
            bright=True
        )

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if successful:

        bprint(
            "\nDownload Complete!",
            bright=True
        )

        bprint(
            f"\nSaved to:\n"
            f"{DOWNLOAD_FOLDER}"
        )

    else:

        bprint(
            "\nOne or more downloads failed.",
            bright=True
        )

        bprint(
            f"Files may be in:\n"
            f"{DOWNLOAD_FOLDER}"
        )

    return successful


# ============================================================
# QUICK & EASY
# ============================================================

def quick_download():

    bprint(
        "\nQUICK & EASY DOWNLOAD",
        bright=True
    )

    bprint(
        "Highest quality available."
    )

    bprint()

    url = get_url()

    if not url:
        return

    download(

        url,

        fmt=(
            "bestvideo+bestaudio/best"
        ),

        audio_only=False,

        container="mp4"
    )


# ============================================================
# ADVANCED
# ============================================================

def advanced_download():

    bprint(
        "\nADVANCED DOWNLOAD",
        bright=True
    )

    bprint()

    url = get_url()

    if not url:
        return

    # --------------------------------------------------------
    # TYPE
    # --------------------------------------------------------

    bprint(
        "\nDOWNLOAD TYPE",
        bright=True
    )

    bprint(
        "1) Audio"
    )

    bprint(
        "2) Video without audio"
    )

    bprint(
        "3) Video + audio"
    )

    bprint()

    choice = binput(
        "Choose download type: "
    )

    if choice not in (
        "1",
        "2",
        "3"
    ):

        choice = "3"

    # --------------------------------------------------------
    # AUDIO
    # --------------------------------------------------------

    if choice == "1":

        name, container = (
            choose_audio_format()
        )

        bprint(
            f"\nSelected: {name}",
            bright=True
        )

        download(

            url,

            fmt="bestaudio/best",

            audio_only=True,

            container=container
        )

        return

    # --------------------------------------------------------
    # QUALITY
    # --------------------------------------------------------

    quality_name, quality_format = (
        choose_quality()
    )

    # --------------------------------------------------------
    # VIDEO ONLY
    # --------------------------------------------------------

    if choice == "2":

        format_name, container = (
            choose_video_format()
        )

        video_format = (
            quality_format.split("+")[0]
        )

        bprint(
            f"\nQuality: {quality_name}"
        )

        bprint(
            f"Format: {format_name}",
            bright=True
        )

        download(

            url,

            fmt=video_format,

            audio_only=False,

            container=container
        )

        return

    # --------------------------------------------------------
    # VIDEO + AUDIO
    # --------------------------------------------------------

    format_name, container = (
        choose_video_format()
    )

    bprint(
        f"\nQuality: {quality_name}"
    )

    bprint(
        f"Format: {format_name}",
        bright=True
    )

    download(

        url,

        fmt=quality_format,

        audio_only=False,

        container=container
    )


# ============================================================
# MAIN MENU
# ============================================================

def menu():

    while True:

        banner()

        bprint(
            "1) Quick & Easy Download"
        )

        bprint(
            "2) Advanced Download"
        )

        bprint(
            "3) Exit"
        )

        bprint()

        choice = binput(
            "Choose an option: "
        )

        # ----------------------------------------------------
        # QUICK
        # ----------------------------------------------------

        if choice == "1":

            clear_screen()

            quick_download()

        # ----------------------------------------------------
        # ADVANCED
        # ----------------------------------------------------

        elif choice == "2":

            clear_screen()

            advanced_download()

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "3":

            clear_screen()

            bprint(
                "Thanks for using 8K YT Downloader!",
                bright=True
            )

            bprint()

            break

        # ----------------------------------------------------
        # INVALID
        # ----------------------------------------------------

        else:

            bprint(
                "\nInvalid choice."
            )

        bprint()

        input(
            "Press Enter to return to the menu..."
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    try:

        menu()

    except KeyboardInterrupt:

        clear_screen()

        bprint(
            "Exiting...",
            bright=True
        )

    except Exception as error:

        clear_screen()

        bprint(
            "FATAL ERROR",
            bright=True
        )

        bprint(
            str(error)
        )

        input(
            "\nPress Enter to exit..."
        )