import requests
from bs4 import BeautifulSoup
import json

response = requests.get("https://www.instagram.com/p/CVZ7ZyBFggy/").json()
# soup = BeautifulSoup(response, 'lxml')
# link = soup.find("meta", property=property)
# print[link['content']]
# g = response["graphql"]
# print(g)