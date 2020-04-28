# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieScrapItem3
from html_text import extract_text

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    start_urls = ['https://en.wikipedia.org/wiki/List_of_Indian_film_actors']
    custom_settings = {
        'ITEM_PIPELINES': {
            'movie_scrap.pipelines.WikiScrapPipeline': 400
        }
    }

    def parse(self, response):
        links = response.css('.column-width a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback = self.get_info)

    def get_info(self, callback):
        items  = MovieScrapItem3()
        name = callback.css('#firstHeading::text')[0].extract()
        try:
            image = 'http:' + callback.css('.vcard img::attr(src)')[0].extract()
        except Exception as e:
            image = None
        born = callback.css('tr:nth-child(3) td span::text')[1].extract()
        content = callback.css('.vcard+ p')
        for para in content:
            html = para.get()
            bio = extract_text(html)
        items['name'] = name
        items['image'] = image
        items['born'] = born
        items['bio'] = bio
        yield items