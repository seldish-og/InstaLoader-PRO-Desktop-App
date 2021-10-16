import random
import time
import lxml
import cchardet
import os
import requests
import requests.exceptions
from bs4 import BeautifulSoup


class Initializer:
    def __init__(self, video_name, video_path, mode, url):
        self.VIDEO_NAME = video_name
        self.PATH = video_path
        self.MODE = mode
        self.URL = url
        self.HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/87.0.4280.141 Safari/537.36',
                        'accept': '*/*'}


class TextParser(Initializer):
    def get_page_text(self, url):
        try:
            requests_session = requests.Session()
            response = requests_session.get(url, headers=self.HEADERS)
            return response.text

        except requests.exceptions.MissingSchema:
            return "Invalid Url" 

    def get_link(self):
        html = self.get_page_text(self.chat_url)
        soup = BeautifulSoup(html, 'lxml')
        if self.MODE == "video":
            property = "og:video"
        if self.MODE == "picture":
            property = f"og:image"
        link = soup.find("meta", property=property)
        return link['content']


class Downloader(Initializer):
    def download_video(self, link):
        video = requests.get(link, stream=True)
        complete_name = os.path.join(self.PATH, self.VIDEO_NAME)

        with open(complete_name, "wb") as video_file:
            for chunk in video.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    video_file.write(chunk)
        return f"Video successfully saved!"


t = Downloader("saundezy1.mp4", r"C:\Users\jegor\Downloads", "photo", "https://www.instagram.com/p/CU4Y1DtF0zM/", 2)
t.download_video()
