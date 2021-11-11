from .downloader import Downloader, TextParser


def main(video_name, video_path, mode, link, width, height):
    text_parser = TextParser(link, mode)
    downloader = Downloader(video_name, video_path, width, height)

    url = text_parser.get_url()
    if mode == "video":
        downloader.download_video(url)
    if mode == "image":
        downloader.download_image(url)
