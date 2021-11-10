import requests
from bs4 import BeautifulSoup as bs
import json
import selenium
from selenium import webdriver
import re
from skimage import io
import cv2
from PIL import Image
from io import BytesIO
from datetime import datetime 

x = str(datetime.now()).split()
print(f"{x[1][:-10]}/{x[0]}")
# url = 'https://scontent-arn2-1.cdninstagram.com/v/t50.16885-16/254332802_261172062631603_6019715270867718089_n.mp4?_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=107&_nc_ohc=s4ttind-S2sAX9ruxyX&edm=AABBvjUBAAAA&ccb=7-4&oe=618CD743&oh=e0e061a4c68e5e9135a445e30aa034de&_nc_sid=83d603'
# r = requests.get(url)
# with open(r"C:\Users\jegor\Downloads\filename.mp4", "wb") as filee:
#     for chunk in r.iter_content(chunk_size = 1024*1024): 
#             if chunk: 
#                 filee.write(chunk) 
 

'''doesn't work'''
# width,height = '500', '600'
# req = io.imread("https://www.instagram.com/p/CVykxdThgHP/")
# cv2.imwrite(r"C:\Users\jegor\Downloads\imagexr.jpg", cv2.resize(req, (400,500)))
'''doesn't work'''

'''work well both with pics and vids'''
# response = requests.get("https://www.instagram.com/p/CV2FxakF7Rl/").text

# match = re.findall('"video_url":"([^"]+)"', response)
# a = match[0].replace("\\u0026", "&")
# print(a)
# print(requests.get(a))
'''work well'''


'''not tested'''
# if response.ok:
#     html=response.text
 
#     bs_html= bs(html, features="lxml")
#     bs_html= bs_html.text
#     index=bs_html.find('profile_pic_url_hd')+21
 
#     remaining_text=bs_html[index:]
#     remaining_text_index=remaining_text.find('requested_by_viewer')-3
#     string_url=remaining_text[:remaining_text_index].replace("\\u0026","&")
 
#     print(string_url, "\n \n downloading..........")
'''not tested'''



'''work but its a webdriver'''
# driver = webdriver.Chrome('chromedriver')
# driver.get("https://www.instagram.com/p/CVykxdThgHP/")

# soup = bs(driver.page_source, 'lxml')

# img = soup.find('img', class_='FFVAD')
# img_url = img['src']

# print(img_url)
'''work but its a webdriver'''
