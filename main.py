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

    res = input("144p 240p 360p 480p 720p 1080p: ")

    if res == "144p":
        yt.streams.filter(res="144p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "240p":
        yt.streams.filter(res="240p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "360p":
        yt.streams.filter(res="360p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "480p":
        yt.streams.filter(res="480p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "720p":
        yt.streams.filter(res="720p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    # without p

    if res == "144":
        yt.streams.filter(res="144p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "240":
        yt.streams.filter(res="240p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "360":
        yt.streams.filter(res="360p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "480":
        yt.streams.filter(res="480p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")

    elif res == "720":
        yt.streams.filter(res="720p").first().download()

        print("")

        print(yt.title + " has been successfully downloaded.")
