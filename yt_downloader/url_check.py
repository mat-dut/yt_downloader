import requests


def check_url(video_url):
    request = requests.get("https://www.youtube.com/oembed?url="+video_url)

    return request.status_code == 200
