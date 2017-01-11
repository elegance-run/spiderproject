# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class PythonbeautifulPipeline(object):


    def __init__(self):
        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        db_name = settings['MONGO_DB']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGO_COLL']]




    def process_item(self, item, spider):

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.post.insert(dict(item))

        return item
