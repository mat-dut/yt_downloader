from __future__ import unicode_literals
from genericpath import exists
import yt_dlp
import os
import time
import json
from tkinter import filedialog
from tkinter import *
import url_check
import config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.withdraw()

if not os.path.exists('data.json'):

    print("Choose default destination folder:")

    folder_selected = filedialog.askdirectory()
    while folder_selected == "":
        folder_selected = filedialog.askdirectory()

    with open('data.json', 'w') as f:
        data = {
            'path': f'{folder_selected}'
        }
        json.dump(data, f)

mode = 'mp3'
input_text = 'mp4'

if not os.path.exists('downloads'):
    os.mkdir('downloads')

links = []
q = ''

while q != "e":

    ydl_opts = config.return_config(mode)

    DEFAULT_PATH = ydl_opts['DEFAULT_PATH']

    q = input(
        f"Insert links \n *-download given links\n l-clear links list\n c-clear default dir\n m-switch to {input_text}\n d-change default dir (current: {DEFAULT_PATH})\n e-exit\n{links}\n: ")

    if q == 'c':
        for i in os.listdir(DEFAULT_PATH):
            if i.endswith('.mp3') or i.endswith('.mp4'):
                os.remove(f'{DEFAULT_PATH}/{i}')

    elif q == '*':
        if not links:
            print("List is empty!")
            time.sleep(1)
        else:
            if mode == 'mp3':
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(links)
            else:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download(links)
        print("Done!")
        time.sleep(1)
        links.clear()

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
        folder_selected = filedialog.askdirectory()

        with open('data.json', 'w') as f:
            data = {
                'path': f'{folder_selected}'
            }
            json.dump(data, f)

    else:
        if url_check.check_url(q):
            links.append(q)
        else:
            print("Invalid URL!")
            time.sleep(1)

    os.system('cls')
