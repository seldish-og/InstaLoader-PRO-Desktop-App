from downloader import TextParser
from downloader import Downloader, TextParser


def main(video_name, video_path, mode, url, width, height):
    text_parser = TextParser(url, mode)
    downloader = Downloader(video_name, video_path, width, height)

    link = text_parser.get_link()
    downloader.download(link)

if __name__ == '__main__':
    main("testphoto.png", r"C:\Users\jegor\Downloads",
     "picture", "https://www.instagram.com/p/CVykxdThgHP/",
      "400", "500")

