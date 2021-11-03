import lxml
import cchardet
import os
import requests
import requests.exceptions
from bs4 import BeautifulSoup


class TextParser:
    def __init__(self, url, mode):
        self.url = url
        self.mode = mode

    def get_page_text(self, url):
        try:

            requests_session = requests.Session()
            response = requests_session.get(url)

            return response.text

        except requests.exceptions.MissingSchema:
            return "Invalid Url" 

    def get_link(self):
        html = self.get_page_text(self.url)
        soup = BeautifulSoup(html, 'lxml')

        if self.mode == "video":
            property = "og:video"

        if self.mode == "picture":
            property = f"og:image"

        link = soup.find("meta", property=property)
        return link['content']


class Downloader:
    def __init__(self, video_name, video_path, width, height):
        self.VIDEO_NAME = video_name
        self.PATH = video_path
        self.WIDTH = width
        self.HEIGHT = height

    def download(self, link):
        try:
            video = requests.get(link, stream=True)
        except requests.exceptions.MissingSchema:
            return "Invalid Url" 

        complete_name = os.path.join(self.PATH, self.VIDEO_NAME)

        with open(complete_name, "wb") as video_file:

            for chunk in video.iter_content(chunk_size=self.WIDTH * self.HEIGHT):
                if chunk:
                    video_file.write(chunk)

        print("successfully saved!")
