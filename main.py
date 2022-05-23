import os
import time
from tkinter import filedialog
from tkinter import *
from url_check import check_url
import config
import downloader
import get_directory
from save_to_json import save_to_json


def main():

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FILENAME = 'data.json'

    root = Tk()
    root.withdraw()

    if not os.path.exists(DATA_FILENAME):

        print("Choose default destination folder:")

        folder_selected = get_directory.get_dir()

        data = {
            'path': f'{folder_selected}'
        }
        save_to_json(DATA_FILENAME, data)

    mode = 'mp3'
    input_text = 'mp4'

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
                downloader.download(links, ydl_opts)
            print("Done!")
            time.sleep(1)
            links.clear()

        elif q == 'e':
            quit()

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
            folder_selected = get_directory.get_dir()

            data = {
                'path': f'{folder_selected}'
            }

            save_to_json(DATA_FILENAME, data)

        else:
            if check_url(q):
                links.append(q)
            else:
                print("Invalid URL!")
                time.sleep(1)

        os.system('cls')


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        import main_commandLine
        main_commandLine.run()
    else:
        main()
