import lxml
import cchardet
import re
import os
import requests
import requests.exceptions
from bs4 import BeautifulSoup


class TextParser:
    def __init__(self, url, mode):
        self.URL = url
        self.MODE = mode

    def get_page_text(self, url):
        try:

            requests_session = requests.Session()
            response = requests_session.get(url)

            return response.text

        except requests.exceptions.MissingSchema:
            return "Invalid Url" 

    def get_link(self):
        response = self.get_page_text(self.URL)
        matches = re.findall(r"video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count", response)
        refactored_matches = matches[0].replace("\\u0026", "&")

        if self.MODE == "video":
            print(2)
            links = refactored_matches.split('''"''')
            main_link = links[0]
 
        if self.MODE == "picture":
            pass

        print(main_link)
        return main_link


class Downloader:
    def __init__(self, video_name, video_path, width, height):
        self.VIDEO_NAME = video_name
        self.PATH = video_path
        self.WIDTH = int(width)
        self.HEIGHT = int(height)

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
