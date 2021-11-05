import requests
from bs4 import BeautifulSoup
import json
import re

response = requests.get("https://www.instagram.com/p/CVPqgYjl-eU/").text

# match = re.findall(r"video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count", response)
# a = match[0].replace("\\u0026", "&")
# print(requests.get(a))


match = re.findall(r"video_url\W\W\W([-\W\w]+)\W\W\Wvideo_view_count", response)
a = match[0].replace("\\u0026", "&")

x = a.split('''"''')
print(x[0])
'''274
   275
   '''