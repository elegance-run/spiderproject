from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
douban = client['douban']
item_info = douban['item_info']
urls = ['https://movie.douban.com/tag/爱情?start={}&type=T'.format(str(i)) for i in range(0,1500,20)]

#https://movie.douban.com/tag/爱情?start=40&type=T



def get_attractions(url, data=None):
    wb_data = requests.get(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('.pl2 a span')
    descriptions = soup.select('.pl2 p')
    cates  = soup.select('.rating_nums')if len(soup.select('.rating_nums')) else None

    if data == None:
        for title, description, cate in zip(titles, descriptions, cates):
            data = {
                'title': title.get_text().strip(),
                'description': description.get_text().strip(),
                'cate': list(cate.stripped_strings),
                }
            item_info.insert_one(data)
        print(data)




for single_url in urls:
    get_attractions(single_url)





