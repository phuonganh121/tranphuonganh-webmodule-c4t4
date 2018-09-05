# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import pyexcel
# news_items=[]
# for i in range(11):
#     if i == 1:
#         continue
#     url = "www.bepthucduong.com/category/mon-an-chay-thuc-duong/mon-an-noi-bat/page/{0}".format(i)
#     connection = urlopen(url)
#     raw_data = connection.read()
#     text = raw_data.decode('utf=8')

#     soup = BeautifulSoup(text, 'html.parser')

#     div_food = soup.find('div', 'cp-news-grid-style-5 m30')
#     # print(ul_food)
#     ul_food = div_food.find_all('ul','small-grid')

    
#     for ul in ul_food:
#         for li in ul:
#             a = li.find('a')
#             if a != -1 :
#                 image = a.img['src']
#                 link = url + a['href']
#                 title = a['title']

#                 item = {
#                 "image": image,
#                 "link": link,
#                 'title': title
#                 }
#                 news_items.append(item)

# pyexcel.save_as(records=news_items, dest_file_name='btd1.xlsx')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
news_items=[]
for i in range(11):
    if i == 1:
        continue
    url = "http://www.bepthucduong.com/category/mon-an-chay-thuc-duong/mon-an-noi-bat/page/{0}/".format(i)
    connection = urlopen(url)
    raw_data = connection.read()
    text = raw_data.decode('utf=8')

    soup = BeautifulSoup(text, 'html.parser')

    div_food = soup.find('div', 'cp-news-grid-style-5 m30')
    # print(ul_food)
    ul_food = div_food.find_all('ul','small-grid')

    for ul in ul_food:
        for li in ul:
            a = li.find('a')
            if a != -1 :
                image = a.img['src']
                link = url + a['href']
                title = a['title']

                item = {
                "image": image,
                "link": link,
                'title': title
                }
                news_items.append(item)

pyexcel.save_as(records=news_items, dest_file_name='btd1.xlsx')
