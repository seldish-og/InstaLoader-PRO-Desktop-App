import os
import re
from io import BytesIO

import requests
import requests.exceptions
from PIL import Image


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

    def get_url(self):
        response = self.get_page_text(self.URL)

        if self.MODE == "video":
            matches = re.findall('"video_url":"([^"]+)"', response)

        if self.MODE == "image":
            matches = re.findall('"display_url":"([^"]+)"', response)

        main_url = matches[0].replace("\\u0026", "&")
        print(main_url)
        return main_url


class Downloader:
    def __init__(self, video_name, video_path, width, height):
        self.WIDTH = int(width)
        self.HEIGHT = int(height)
        self.COMPLETE_PATH = os.path.join(video_path, video_name)

    def download_image(self, link):
        try:
            response = requests.get(link)
        except requests.exceptions.MissingSchema:
            return "Invalid Url"

        image = Image.open(BytesIO(response.content))
        resized_image = image.resize((self.WIDTH, self.HEIGHT), Image.ANTIALIAS)
        resized_image.save(self.COMPLETE_PATH)

        print("successfully saved!")

    def download_video(self, link):
        try:
            video = requests.get(link, stream=True)
        except requests.exceptions.MissingSchema:
            return "Invalid Url"

        with open(self.COMPLETE_PATH, "wb") as video_file:
            for chunk in video.iter_content(chunk_size=900 * 900):
                if chunk:
                    video_file.write(chunk)

        print("successfully saved!")
