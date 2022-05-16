from __future__ import unicode_literals
from genericpath import exists
import yt_dlp
import os
import yt_dlp
import time
import json
from tkinter import filedialog
from tkinter import *

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists('data.json'):

    with open('data.json', 'w') as f:
        data = {
            "path": f"{ROOT_DIR}/contents"
        }
        json.dump(data, f)

mode = 'mp3'
input_text = 'mp4'

DEFAULT_PATH = ''

with open('data.json', 'r') as f:
    data = json.load(f)
    DEFAULT_PATH = data['path']

ydl_opts_mp3 = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': f'{DEFAULT_PATH}/%(title)s.%(ext)s',
}

ydl_opts_mp4 = {
    'postprocessors': [{
        'key': 'FFmpegMetadata',
    }],
    'outtmpl': f'{DEFAULT_PATH}/%(title)s.%(ext)s',
}

if not os.path.exists('contents'):
    os.mkdir('contents')


links = []
q = ''

while q != "e":
    q = input(
        f"Insert links \n *-download given links\n l-clear links list\n c-clear default dir\n m-switch to {input_text}\n d-change default dir\n e-exit\n{links}\n: ")

    if q == 'c':
        for i in os.listdir('contents'):
            if i.endswith('.mp3') or i.endswith('.mp4'):
                os.remove(f'contents/{i}')

    elif q == '*':
        if not links:
            print("List is empty!")
            time.sleep(1)
        else:
            if mode == 'mp3':
                with yt_dlp.YoutubeDL(ydl_opts_mp3) as ydl:
                    ydl.download(links)
            else:
                with yt_dlp.YoutubeDL(ydl_opts_mp4) as ydl:
                    ydl.download(links)

    elif q == 'e':
        exit()

    elif q == 'l':  # lowercase L
        links = []

    elif q == 'm':
        if mode == 'mp3':
            mode = 'mp4'
            input_text = 'mp3'
        else:
            mode = 'mp3'
            input_text = 'mp4'

    elif q == 'd':

        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()

        with open('data.json', 'w') as f:
            data = {
                'path': f'{folder_selected}'
            }
            json.dump(data, f)

    else:
        links.append(q)

    os.system('cls')
