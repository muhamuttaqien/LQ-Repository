# -*- coding: utf-8 -*-
import scrapy


class KonsultasisyariahSpider(scrapy.Spider):
    name = 'konsultasisyariah'
    allowed_domains = ['konsultasisyariah.com']
    start_urls = ['http://konsultasisyariah.com/']

    def parse(self, response):
        pass
