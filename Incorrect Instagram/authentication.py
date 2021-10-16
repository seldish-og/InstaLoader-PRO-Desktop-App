import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Initializer:
    def __init__(self, username, password, mode, chat_url, quantity):
        self.username = username
        self.password = password
        self.mode = mode
        self.chat_url = chat_url
        self.quantity = quantity

        mobile_emulation = {
            "deviceName": "iPhone X"
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.browser = webdriver.Chrome(
            executable_path='chromedriver',
            options=chrome_options)

    def delay(self, delay_start, delay_finish):
        time.sleep(random.randrange(delay_start, delay_finish))

    def close_browser(self):
        self.browser.close()
        self.browser.quit()  # (just in case)


class Login(Initializer):
    def login(self):  # login to the account
        try:
            self.browser.get('https://www.instagram.com/accounts/login/?next=%2F&source=mobile_nav')
            self.delay(2, 5)

            user_input = self.browser.find_element_by_name('username')
            user_input.clear()
            user_input.send_keys(self.username)
            self.delay(2, 5)

            password_input = self.browser.find_element_by_name('password')
            password_input.clear()
            password_input.send_keys(self.password)
            self.delay(2, 5)

            password_input.send_keys(Keys.ENTER)
            self.delay(2, 5)
        except Exception:
            print('Problem with login')
            self.close_browser()
