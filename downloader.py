from pytubefix import YouTube

url = input("Cole a sua url: ")

try:
    video = YouTube(url)
except:
    print("Ocorreu um erro")

mp4_streams = video.streams.get_highest_resolution()

mp4_streams.download()
