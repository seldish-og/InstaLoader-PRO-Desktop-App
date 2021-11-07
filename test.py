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

url = 'https://scontent-arn2-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/252491310_406986530867116_404895148171725041_n.jpg?_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=104&_nc_ohc=19PscMIOfV4AX9CEqHh&edm=AABBvjUBAAAA&ccb=7-4&oh=7fb20cd9a2a30362aacd4f51a32435c2&oe=618E0064&_nc_sid=83d603.jpg'
r = requests.get(url)
image = Image.open(BytesIO(r.content))
new_image = image.resize((400, 500), Image.ANTIALIAS)
new_image.save('image_400.jpg')


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
