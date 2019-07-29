# -*- coding: utf-8 -*-

import json
import os

from scrapy.pipelines.images import ImagesPipeline
from jav_bus_spider_scrapy.items import JavSpiderByScrapyImagesItem, JavSpiderByScrapyItem
import redis


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JavSpiderByScrapyPipeline(object):
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db
        self.pool = None
        self.redis = None
        self.pipe = None

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        host = settings.get('REDIS_HOST', '172.17.0.1')
        port = settings.get('REDIS_PORT', 6379)
        db = settings.get('REDIS_DB', 0)
        return cls(host=host, port=port, db=db)

    def open_spider(self, spider):
        _ = spider
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)
        self.redis = redis.StrictRedis(connection_pool=self.pool)
        self.pipe = self.redis.pipeline(transaction=False)

    def close_spider(self, spider):
        _ = spider
        self.pipe.execute()
        self.pool.disconnect()

    def process_item(self, item, spider):
        if isinstance(item, JavSpiderByScrapyImagesItem):
            return item
        elif isinstance(item, JavSpiderByScrapyItem):
            _ = self, spider  # 无实际意义
            designation = item.get('designation')

            magnet_infos = item.get('magnet_infos') or [{'name': '', 'size': '', 'time': '', 'link': ''}]
            sample_list = item.get('sample_list')
            details = json.dumps(dict(mi=magnet_infos, sl=sample_list), ensure_ascii=False)

            self.pipe.hmset(
                'l_{}'.format(designation),
                dict(
                    d=designation,
                    dt=item.get('designation_title'),
                    pt=item.get('publish_time'),
                    sn=item.get('star_name'),
                    mc=len(item.get('magnet_infos')),  # magnet_count
                    sc=len(item.get('sample_list')),  # sample_count
                    il=0,  # is_like
                )
            )
            self.pipe.set('d_{}'.format(designation), details)
            return item


class JavSpiderByScrapyImagesPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        if isinstance(item, JavSpiderByScrapyImagesItem):
            return super().process_item(item, spider)

    def get_media_requests(self, item, info):
        request_objs = super().get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        designation = request.item.get('designation')
        designation_dir = designation  # 使用番号作为目录名
        if 'cover' in request.url:
            image_name = ''.join((designation, '.jpg'))
        else:
            image_name = request.url.split('/')[-1]

        image_path = os.path.join(designation_dir, image_name)
        return image_path
