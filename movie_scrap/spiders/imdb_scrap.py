import scrapy
from ..items import MovieScrapItem

class imdb_scrap(scrapy.Spider):
    name = "imdb_scrap"
    start_urls = [
        "https://www.imdb.com/list/ls068010962/"
    ]
    custom_settings = {
        'ITEM_PIPELINES': {
            'movie_scrap.pipelines.MovieScrapPipeline': 400
        }
    }

    def parse(self, response):
        links = response.css('.lister-item-header a::attr(href)').extract()
        for link in links:
            yield response.follow(link, callback = self.get_info)

    def get_info(self, callback):
        items  = MovieScrapItem()
        name = callback.css('.header .itemprop::text')[0].extract()
        try:
            image = callback.css('#name-poster::attr(src)')[0].extract()
        except Exception as e:
            image = None
        
        born = callback.css('time::attr(datetime)')[0].extract()
        prof = callback.css('#name-job-categories .itemprop::text').extract()
        professions = []
        for profession in prof:
            professions.append(profession.strip())
        bio = callback.css('#name-bio-text .inline::text').extract()[0].strip()
        

        items['name'] = name
        items['image'] = image
        items['birth_date'] = born
        items['professions'] = professions
        items['bio'] = bio
        yield items