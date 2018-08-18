from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode('utf=8')

soup = BeautifulSoup(text, 'html.parser')

section_songs = soup.find('section', 'section chart-grid')

li_list = section_songs.find_all('li')

news_items=[]
for li in li_list:
    a = li.a 
    name = li.h3.a.text
    artist = li.h4.a.text
    item = {
        "name": name,
        "artist": artist
    }
    news_items.append(item)

pyexcel.save_as(records=news_items, dest_file_name='sample1.xlsx')
