import pytube
from pytube import YouTube
import os

# url input from user
yt = YouTube(
    str(input("URL: \n>> ")))

mp3_or_mp4 = input("mp3 or mp4? mp3/mp4: ")

if mp3_or_mp4 == "mp3":

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # download the file
    out_file = video.download()

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")

elif mp3_or_mp4 == "mp4":

    # download the file
    stream = yt.streams.first()
    stream.download()

    print("")

    # result of success
    print(yt.title + " has been successfully downloaded.")
