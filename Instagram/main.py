from downloader import TextParser
from downloader import Downloader, TextParser


def main(video_name, video_path, mode, url):
    text_parser = TextParser(url, mode)
    downloader = Downloader(video_name, video_path)

    link = text_parser.get_link()
    downloader.download(link)

if __name__ == '__main__':
    main(name, path, mode, 
    link)

