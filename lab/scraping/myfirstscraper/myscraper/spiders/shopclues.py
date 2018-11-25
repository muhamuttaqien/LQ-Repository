
# coding: utf-8

# In[ ]:


import scrapy

class ShopcluesSpider(scrapy.Spider):
    # name of spider
    name = 'shopclues'

    # list of allowed domains
    allowed_domains = ['www.shopclues.com/mobiles-feature-phones.html']
    #starting url
    start_urls = ['https://www.shopclues.com/mobiles-feature-phones.html?sort_by=sort_price&sort_order=asc&facet_brand[]=Ikall&fsrc=facet_brand/']
    # location of csv file
    custom_settings = {
        'FEED_URI' : 'tmp/shopclues.csv',
        'FEED_FORMAT': 'csv'
    }

    def parse(self, response):
        print('starts crawling...')
        
        # extract product information
        titles = response.css('.column.col3 h2::text').extract()
        prices = response.css('.column.col3 .p_price::text').extract()
        discounts = response.css('.column.col3 .prd_discount::text').extract()
        images = response.css('img::attr(data-img)').extract()
        
        for item in zip(titles, prices, discounts, images):
            scraped_info = {
                'titles' : item[0],
                'prices' : item[1],
                'discounts' : item[2],
                'image_urls' : [item[3]],
            }

            yield scraped_info