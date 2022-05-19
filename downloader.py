import yt_dlp


def download(links, options):
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(links)
