# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnalyticsItem(scrapy.Item):
	 # define the fields for your item here like:
    # name = scrapy.Field()
    comapny_name       = scrapy.Field()
    min_project_size   = scrapy.Field()
    hourly_rate        = scrapy.Field()
    employee           = scrapy.Field()
    founded_year       = scrapy.Field()
    location           = scrapy.Field()
    rating             = scrapy.Field()
   
    pass
