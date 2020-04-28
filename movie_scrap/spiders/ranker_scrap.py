# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieScrapItem2


class RankerScrapSpider(scrapy.Spider):
    name = 'ranker_scrap'
    page_number = 2
    start_urls = ['https://www.ranker.com/list/film-actors-from-india/reference?page=1']
    custom_settings = {
        'ITEM_PIPELINES': {
            'movie_scrap.pipelines.RankerScrapPipeline': 400
        }
    }

    def parse(self, response):
        items  = MovieScrapItem2()
        actors = response.css('.listItem')
        for actor in actors:
            name = actor.css('.listItem__title::text')[0].extract()
            try:
                image = actor.css('.lozad::attr(data-src)')[0].extract()
            except Exception as e:
                image = None
            age_credit = actor.css('.listItem__properties::text')[0].extract()
            if age_credit.split(' ')[1] == 'Age':
                age = age_credit.split(' ')[2].split(',')[0]
            else:
                age = age_credit.split(' ')[3] + ', at the time of death'
            credit = age_credit.split(':')[-1]
            bio = actor.css('.listItem__wiki::text')[0].extract()
            items['name'] = name
            items['image'] = image
            items['age'] = age
            items['credit'] = credit
            items['bio'] = bio
            yield items

            next_page = 'https://www.ranker.com/list/film-actors-from-india/reference?page=' + str(RankerScrapSpider.page_number)
            if RankerScrapSpider.page_number <= 50:
                RankerScrapSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)
            
