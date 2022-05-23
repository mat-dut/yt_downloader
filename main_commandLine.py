import argparse
import downloader
import config


def run():

    parser = argparse.ArgumentParser(description='yt_downloader')

    parser.add_argument(
        "-L", "--links", help="links seperated with a space", required=True, nargs="*")

    parser.add_argument('-M', '--mode', help='mp3 or mp4', required=True)

    parser.add_argument('-D', '--destination',
                        help='destination folder', required=True)

    args = parser.parse_args()

    links = args.links
    mode = args.mode
    destination = args.destination

    ydl_opts = config.return_config(mode, destination)

    downloader.download(links, ydl_opts)
