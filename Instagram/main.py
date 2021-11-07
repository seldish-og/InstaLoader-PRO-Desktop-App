from downloader import TextParser
from downloader import Downloader, TextParser


def main(video_name, video_path, mode, url, width, height):
    text_parser = TextParser(url, mode)
    downloader = Downloader(video_name, video_path, width, height)

    link = text_parser.get_link()
    if mode == "video":
        downloader.download_video(link)
    if mode == "image":
        downloader.download_image(link)

if __name__ == '__main__':
    main("testphoto21.png", r"C:\Users\jegor\Downloads",
     "image", "https://www.instagram.com/p/CVykxdThgHP/",
      "400", "500")

