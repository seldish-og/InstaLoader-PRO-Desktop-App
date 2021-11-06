import requests
from bs4 import BeautifulSoup as bs
import json
import selenium
from selenium import webdriver
import re
from skimage import io
import cv2


width,height = '500', '600'
req = io.imread("https://www.instagram.com/p/CVykxdThgHP/")
cv2.imwrite(r"C:\Users\jegor\Downloads\image.jpg", cv2.resize(req, (width,height)))

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
