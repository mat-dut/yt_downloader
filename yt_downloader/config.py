import json


def return_config(file_type="mp3", destination_folder=None):

    if destination_folder != None:
        DEFAULT_PATH = destination_folder
    else:
        with open('data.json', 'r') as f:
            data = json.load(f)
            DEFAULT_PATH = data['path']

    if file_type == "mp3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'outtmpl': f'{DEFAULT_PATH}/%(title)s.%(ext)s',
            'DEFAULT_PATH': DEFAULT_PATH,
            'quiet': True,
        }

    elif file_type == "mp4":
        ydl_opts = {
            'postprocessors': [{
                'key': 'FFmpegMetadata',
            }],
            'outtmpl': f'{DEFAULT_PATH}/%(title)s.%(ext)s',
            'DEFAULT_PATH': DEFAULT_PATH,
            'quiet': True,
        }

    return ydl_opts
