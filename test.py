import requests
from bs4 import BeautifulSoup
import json
import re

response = requests.get("https://www.instagram.com/p/CVZ7ZyBFggy/").text
match = re.findall(r"video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count", response)
a = match[0].replace("\\u0026", "&")
print(requests.get(a))

''' Everything works add and test same func for image, and replace old download method in downloader.py'''