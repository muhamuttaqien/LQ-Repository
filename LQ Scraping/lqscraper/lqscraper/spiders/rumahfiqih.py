# -*- coding: utf-8 -*-
import scrapy


class RumahfiqihSpider(scrapy.Spider):
    name = 'rumahfiqih'
    allowed_domains = ['rumahfiqih.com']
    start_urls = ['http://rumahfiqih.com/']

    def parse(self, response):
        pass
