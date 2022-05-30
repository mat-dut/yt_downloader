# yt_downloader

Paste YT URL's and download mp3/mp4 files

* Using [yt-dlp](https://github.com/yt-dlp/yt-dlp)

* FFmpeg executables are required! [Download](https://ffmpeg.org/download.html)

## **Command line functions**

```x
  -h, --help                                show this help message and exit
  -L [LINKS ...], --links [LINKS ...]       links seperated with a space
  -M MODE, --mode MODE                      mp3 or mp4
  -D DESTINATION, --destination DESTINATION destination folder

```

## **Use as a package**

```python
from yt_downloader import downloader
from yt_downloader.config import return_config

options = return_config('mp3') # Used to configure download configuration -return_config(mode, destination)

downloader.download(['https://www.youtube.com/watch?v=dQw4w9WgXcQ'], options) # Put links in a list

```
