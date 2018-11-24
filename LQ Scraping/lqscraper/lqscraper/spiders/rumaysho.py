# -*- coding: utf-8 -*-
import scrapy


class RumayshoSpider(scrapy.Spider):
    name = 'rumaysho'
    allowed_domains = ['rumaysho.com']
    start_urls = ['http://rumaysho.com/',
                  'https://rumaysho.com/18958-hadits-arbain-15-berkata-yang-baik-memuliakan-tamu-dan-tetangga.html']

    custom_settings = {
        'FEED_URI': 'tmp/rumaysho.csv',
    }
    
    def parse(self, response):
        
        # extract article information
        titles = response.css('.td-ss-main-content h1.entry-title::text').extract()
        contents = response.css('.pf-content p').extract()
        
        for item in zip(titles, contents):

            scraped_info = {
                'titles': item[0],
                'contents': contents
            }
            
            yield scraped_info