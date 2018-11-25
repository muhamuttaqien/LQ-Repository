# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ElectronicsSpider(CrawlSpider): # in order to make the crawler navigate to many page, use CrawlSpider insted of scrapy.Spider
    name = "electronics"
    allowed_domains = ["www.olx.com.pk"]
    start_urls = [
        'https://www.olx.com.pk/computers-accessories/',
        'https://www.olx.com.pk/tv-video-audio/',
        'https://www.olx.com.pk/games-entertainment/'
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)

        item_links = response.css('.large > .detailsLink::attr(href)').extract()
        for a in item_links:
            yield scrapy.Request(a, callback=self.parse_detail_page)
            
    def parse_detail_page(self, response):
        title = response.css('h1::text').extract()[0].strip()
        price = response.css('.pricelabel > strong::text').extract()[0]
        item = OlxItem()
        item['title'] = title
        item['price'] = price
        item['url'] = response.url
        
        yield item