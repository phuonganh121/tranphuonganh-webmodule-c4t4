import pyexcel
import crawl.

news = [
    {
        "link": "http://google.com",
        "title": "Google"
    },
    {
        "link": "http://google.com",
        "title": "Google"
    },
    {
        "link": "http://google.com",
        "title": "Google"
    },
]

pyexcel.save_as(records=news, dest_file_name='sample.xlsx')