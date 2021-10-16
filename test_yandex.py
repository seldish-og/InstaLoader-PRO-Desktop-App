import requests

video_src_url = "https://scontent-arn2-1.cdninstagram.com/v/t50.2886-16/245184261_455289922525816_2452910830099063197_n.mp4?_nc_ht=scontent-arn2-1.cdninstagram.com&_nc_cat=104&_nc_ohc=1sz32oyHea4AX8WHJ6_&edm=AABBvjUBAAAA&ccb=7-4&oe=61670D05&oh=e40682947821c49509126a4e397f01b6&_nc_sid=83d603"
video = requests.get(video_src_url, stream=True)
with open('saundezy.mp4', "wb") as video_file:
    for chunk in video.iter_content(chunk_size=1024 * 1024):
        if chunk:
            video_file.write(chunk)
print(f"successfully saved!")
