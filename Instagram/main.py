from downloader import TextParser
from downloader import Downloader, TextParser


def main(video_name, video_path, mode, url, width, height):
    text_parser = TextParser(url, mode)
    downloader = Downloader(video_name, video_path, width, height)

    link = text_parser.get_link()
    print(link)
    downloader.download(link)
    print(1)

if __name__ == '__main__':
    main("testvideo.mp4", r"C:\Users\jegor\Downloads",
     "video", "https://www.instagram.com/p/CV2FxakF7Rl/",
      "1920", "1080")

