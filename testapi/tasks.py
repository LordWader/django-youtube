import requests
import json

from testapi.celery import app

from testapi.models import KeyWordData, YouTubeVideo

SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
DEVELOPER_KEY = "AIzaSyCmq9ngxNoyz2fjLMtz5wZDIcR93xZhhRI"


@app.task
def search_func():
    for item in KeyWordData.objects.all():
        params = {"part": "snippet", "q": item.key_word, "key": DEVELOPER_KEY, "maxResults": 5}
        r = requests.get(SEARCH_URL, params=params)
        string = r.content.decode("utf-8")
        data = json.loads(string)
        urls = set()
        for video in data["items"]:
            try:
                urls.add(f"https://www.youtube.com/watch?v={video['id']['videoId']}")
            except KeyError:
                pass
        videos = set(v[0] for v in item.videos.values_list("url"))
        new_videos = urls - videos
        if new_videos:
            for video in new_videos:
                youtube_url = YouTubeVideo(url=video)
                youtube_url.save()
                item.videos.add(youtube_url)
                item.save()


if __name__ == "__main__":
    search_func()
