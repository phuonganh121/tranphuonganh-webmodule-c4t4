from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://genk.vn"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode('utf=8')

soup = BeautifulSoup(text, 'html.parser')

ul_news = soup.find('ul', 'knsw-list')

li_list = ul_news.find_all('li')

news_items=[]
for li in li_list:
    a = li.a 
    img = li.a.img
    link = url + a['href']
    title = a['title']
    image = img['src']

    item = {
        "title": title,
        "link": link,
        "image": image
    }
    news_items.append(item)

pyexcel.save_as(records=news_items, dest_file_name='genk-crawl.xlsx')


  