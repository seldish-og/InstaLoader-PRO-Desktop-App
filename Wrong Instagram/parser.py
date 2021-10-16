import os
import time

import requests
from selenium.common.exceptions import NoSuchElementException

from Instagram import authentication


class Downloader(authentication.Initializer):
    def xpath_exists(self, url):
        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def get_list_of_hrefs(self, chat_url):
        try:
            self.browser.get(chat_url)
            self.delay(2, 5)

            hrefs = self.browser.find_elements_by_tag_name('a')
            list_of_hrefs = []
            for i in hrefs:
                # extract links from the tag's attribute
                href = i.get_attribute('href')
                # all videos have /p/ in their href
                if '/p/' in href:
                    list_of_hrefs.append(href)
            return list_of_hrefs
        # if something went wrong, close the browser
        except Exception as exc:
            print(exc)
            print("something wrong with links")
            self.close_browser()

    def download_videos(self, page_name, video_number, hrefs, videos_quantity):
        try:
            for number in range(videos_quantity):
                video_number += 1
                self.browser.get(hrefs[number])
                time.sleep(4)
                video_src = "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/div/div/video"

                if self.xpath_exists(video_src):
                    video_src_url = self.browser.find_element_by_xpath(video_src).get_attribute("src")
                    # save video
                    video = requests.get(video_src_url, stream=True)
                    save_folder = "videos"
                    video_name = f"video_{page_name}_{video_number}.mp4"
                    complete_name = os.path.join(save_folder, video_name)
                    with open(complete_name, "wb") as video_file:
                        for chunk in video.iter_content(chunk_size=1024 * 1024):
                            if chunk:
                                video_file.write(chunk)
                    print(f"{hrefs[number]} successfully saved!")
                else:
                    print('error with video xpath')
                    break

        except Exception as exception:
            print(exception)
            print('error with downloading videos ')
            self.close_browser()
