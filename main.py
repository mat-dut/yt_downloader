from __future__ import unicode_literals
from genericpath import exists
import yt_dlp
import os
import yt_dlp


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

ydl_opts_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': f'{ROOT_DIR}/contents/%(title)s.%(ext)s',
}

ydl_opts_mp4 = {
    'postprocessors': [{
        'key': 'FFmpegMetadata',
    }],
    'outtmpl': f'{ROOT_DIR}/contents/%(title)s.%(ext)s',
}

if not os.path.exists('contents'):
    os.mkdir('contents')


links = []
q = ''

while q != "e":
    q = input(
        "Insert links (*-download given links, c-clear contents dir, e-exit): ")

    if q == 'c':
        for i in os.listdir('contents'):
            os.remove(f'contents/{i}')
        continue

    elif q == '*':
        with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
            ydl.download(links)
    elif q == 'e':
        exit()
    else:
        links.append(q)
