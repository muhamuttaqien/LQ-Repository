# -*- coding: utf-8 -*-
import scrapy


class RumayshoPage(scrapy.Spider):
    name = 'rumaysho'
    start_urls = ['https://rumaysho.com/category/belajar-islam']

    custom_settings = {
        'FEED_URI': 'tmp/rumaysho.csv',
    }
    
    def parse(self, response):
        for page_url in response.css('.page-nav a ::attr("href")').extract():
            yield response.follow(page_url, callback=self.parse_page)
            
    def parse_page(self, response):
        for article_url in response.css('.entry-title a ::attr("href")').extract():
            yield response.follow(article_url, callback=self.parse_article)
    
    def parse_article(self, response):
        titles = response.css('.td-ss-main-content h1.entry-title::text').extract()
        content = response.css('.pf-content p').extract()
        yield {'titles': titles, 'contents': ''.join(content)}