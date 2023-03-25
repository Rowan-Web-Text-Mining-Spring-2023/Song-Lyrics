from bs4 import BeautifulSoup
import requests
import re
import lyricsgenius as lg
import os

#Grab top 100 songs from site
url = 'https://top40weekly.com/top-100-songs-of-2021/'
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')
songs = soup.find('ol')

#Genius api for lyrics
api_key= '_MHF5MqhYdAj3Tk3JLx9atl02VFY1tsAaoLPBju4cPEJh0CUw8H3mVbUaD_G9W5tWGPUhO31oqd9n9NLBZsMqQ'
genius = lg.Genius(api_key)
genius.timeout = 15

#Search genius for lyrics and save each file
for song in songs.find_all('li'):
    title = re.search('.* by', str(song.text)).group(0).replace(' by', '').replace('/', '').replace('?', '')
    artist = re.search('by .*', str(song.text)).group(0).replace('by', '')
    f_name = 'lyrics/'+title+'_lyrics.txt'
    if not os.path.isfile(f_name):
        s = genius.search_song(title, artist)
        with open(f_name, 'w', newline='', encoding='utf-8') as file:
            if s is not None:
                file.write(s.lyrics)