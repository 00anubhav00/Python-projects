from pytube import Playlist

link=""
yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.streams.get_highest_resolution().download()
    print(video.title)
