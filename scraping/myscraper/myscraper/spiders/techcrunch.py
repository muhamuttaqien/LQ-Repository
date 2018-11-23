# -*- coding: utf-8 -*-
import scrapy


class TechcrunchSpider(scrapy.Spider):
    name = 'techcrunch'
    allowed_domains = ['techcrunch.com/feed/']
    start_urls = ['http://techcrunch.com/feed//']

    def parse(self, response):
        pass
