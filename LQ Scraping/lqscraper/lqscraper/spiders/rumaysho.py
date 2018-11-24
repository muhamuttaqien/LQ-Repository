# -*- coding: utf-8 -*-
import scrapy


class RumayshoSpider(scrapy.Spider):
    name = 'rumaysho'
    allowed_domains = ['rumaysho.com']
    start_urls = ['http://rumaysho.com/']

    def parse(self, response):
        pass
