# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import gridfs
import mimetypes, requests

class MovieScrapPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['movie_celeb']
        self.collection = db['im_celeb']
        self.grid_fs = gridfs.GridFS(getattr(self.conn, 'movie_celeb'))

    def process_item(self, item, spider):
        if item['image'] is not None:
            mime_type = mimetypes.guess_type(item['image'])[0]
            request = requests.get(item['image'], stream=True)
            _id = self.grid_fs.put(request.raw, contentType=mime_type, filename=item['name'])
            item['image'] = _id
            self.collection.insert(dict(item))
        else:
            self.collection.insert(dict(item))
        return item

class RankerScrapPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['movie_celeb']
        self.collection = db['ranker_celeb']
        self.grid_fs = gridfs.GridFS(getattr(self.conn, 'movie_celeb'))

    def process_item(self, item, spider):
        if item['image'] is not None:
            mime_type = mimetypes.guess_type(item['image'])[0]
            request = requests.get(item['image'], stream=True)
            _id = self.grid_fs.put(request.raw, contentType=mime_type, filename=item['name'])
            item['image'] = _id
            self.collection.insert(dict(item))
        else:
            self.collection.insert(dict(item))
        return item

class WikiScrapPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['movie_celeb']
        self.collection = db['wiki_celeb']
        self.grid_fs = gridfs.GridFS(getattr(self.conn, 'movie_celeb'))

    def process_item(self, item, spider):
        if item['image'] is not None:
            mime_type = mimetypes.guess_type(item['image'])[0]
            request = requests.get(item['image'], stream=True)
            _id = self.grid_fs.put(request.raw, contentType=mime_type, filename=item['name'])
            item['image'] = _id
            self.collection.insert(dict(item))
        else:
            self.collection.insert(dict(item))
        return item