from Instagram.downloader import TextParser
from downloader import Downloader, TextParser, Initializer

text_parser = TextParser()
downloader = Downloader()
initializer = Initializer()

def main():
    link = text_parser.get_link()
    if initializer.MODE == "video":
        downloader.download_video(link)

if __name__ == '__main__':
    main()
