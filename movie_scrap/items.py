# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieScrapItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image = scrapy.Field()
    birth_date = scrapy.Field()
    professions = scrapy.Field()
    bio = scrapy.Field()

class MovieScrapItem2(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image = scrapy.Field()
    age = scrapy.Field()
    credit = scrapy.Field()
    bio = scrapy.Field()

class MovieScrapItem3(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image = scrapy.Field()
    born = scrapy.Field()
    bio = scrapy.Field()
