import random
import time
import os
import requests
import requests.exceptions
from bs4 import BeautifulSoup


class Initializer:
    def __init__(self, video_name, video_path, mode, chat_url, quantity):
        self.video_name = video_name
        self.video_path = video_path
        self.mode = mode
        self.chat_url = chat_url
        self.quantity = quantity
        self.HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                                      ' Chrome/87.0.4280.141 Safari/537.36',
                        'accept': '*/*'}


class Downloader(Initializer):
    def get_page_text(self, url):
        try:
            response = requests.get(url, headers=self.HEADERS)
            return response.text

        except requests.exceptions.MissingSchema:
            return "Invalid Url"

    def find_link(self):
        html = self.get_page_text(self.chat_url)
        soup = BeautifulSoup(html, 'html.parser')
        link = soup.find("meta", property="og:video")
        return link['content']

    def download_video(self):
        video = requests.get(self.find_link(), stream=True)
        complete_name = os.path.join(self.video_path, self.video_name)

        # add checking download mode

        with open(complete_name, "wb") as video_file:
            for chunk in video.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    video_file.write(chunk)
        return f"Video successfully saved!"


t = Downloader("saundezy1.mp4", r"C:\Users\jegor\Downloads", "photo", "https://www.instagram.com/p/CU4Y1DtF0zM/", 2)
t.download_video()
