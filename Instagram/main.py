from downloader import TextParser
from downloader import Downloader, TextParser


def main(video_name, video_path, mode, url, width, height):
    text_parser = TextParser(url, mode)
    downloader = Downloader(video_name, video_path, width, height)

    link = text_parser.get_link()
    downloader.download(link)

if __name__ == '__main__':
    main("testvideo.mp4", r"C:\Users\jegor\Downloads",
     "photo", "https://www.instagram.com/p/CVumcXblduy/",
      "1920", "1080")

