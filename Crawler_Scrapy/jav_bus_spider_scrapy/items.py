# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JavSpiderByScrapyImagesItem(scrapy.Item):
    image_urls = scrapy.Field()
    designation = scrapy.Field()
    images = scrapy.Field()


class JavSpiderByScrapyItem(scrapy.Item):
    designation = scrapy.Field()
    designation_title = scrapy.Field()
    publish_time = scrapy.Field()
    star_name = scrapy.Field()
    magnet_infos = scrapy.Field()
    sample_count = scrapy.Field()
    magnet_count = scrapy.Field()
    url_list = scrapy.Field()
