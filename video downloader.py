from pytube import YouTube

url = "https://www.youtube.com/watch?v=7BXJIjfJCsA "
my_video =YouTube(url)
print(my_video.title)
print(my_video.thumbnail_url)

my_video= my_video.streams.get_highest_resolution()
my_video.download()
