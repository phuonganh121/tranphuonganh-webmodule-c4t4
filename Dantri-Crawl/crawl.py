#1. Download dantri page 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
connection = urlopen(url)
raw_data = connection.read()
text = raw_data.decode('utf=8')
print(text)

# f = open("dantri.html", "w")
# f.write(text)
# f.close()

soup = BeautifulSoup(text, 'html.parser')
print(soup.prettify())

#2. Find the ROI (Region of Interest)

ul_news = soup.find('ul', 'ul1 ulnew')

#3. Extract the date 

li_list = ul_news.find_all('li')

news_items = []
for li in li_list: 
    a = li.h4.a 
    link = url + a['href']
    title = a.text 
    item = {
        "title": title,
        "Link": link
    }
    news_items.append(item)

pyexcel.save_as(records=news_items, dest_file_name='sample1.xlsx')

#4. Save data


