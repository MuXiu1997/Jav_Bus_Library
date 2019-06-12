# -*- coding: utf-8 -*-

import json
import os

from scrapy.pipelines.images import ImagesPipeline

# from jav_bus_spider_scrapy import settings
from jav_bus_spider_scrapy.items import JavSpiderByScrapyImagesItem, JavSpiderByScrapyItem
from models import Session, Info


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class JavSpiderByScrapyPipeline(object):
    def process_item(self, item, spider):
        session = Session()

        if isinstance(item, JavSpiderByScrapyImagesItem):
            return item
        elif isinstance(item, JavSpiderByScrapyItem):
            _ = self, spider  # 无实际意义
            magnet_infos = item.get('magnet_infos')
            if not magnet_infos:
                magnet_infos = [{'name': '', 'size': '', 'time': '', 'link': ''}]
            info_obj = Info(
                designation=item.get('designation'),
                designation_title=item.get('designation_title'),
                publish_time=item.get('publish_time'),
                star_name=item.get('star_name'),
                magnet_infos=json.dumps(magnet_infos, ensure_ascii=False),
                sample_count=item.get('sample_count'),
                magnet_count=item.get('magnet_count'),
                url_list=json.dumps(item.get('url_list'), ensure_ascii=False),
                is_like=False,
            )
            info_find = session.query(Info).filter_by(designation=item.get('designation')).first()
            if info_find:
                session.delete(info_find)
            session.add(info_obj)
            session.commit()
            session.close()
            return item


class JavSpiderByScrapyImagesPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        if isinstance(item, JavSpiderByScrapyItem):
            pass
        elif isinstance(item, JavSpiderByScrapyImagesItem):
            return super().process_item(item, spider)

    def get_media_requests(self, item, info):
        request_objs = super().get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # path = super().file_path(request, response, info)
        designation = request.item.get('designation')
        # images_store = settings.IMAGES_STORE
        # designation_path = os.path.join(images_store, designation)
        designation_path = designation
        if not os.path.exists(designation_path):
            os.mkdir(designation_path)
        if 'cover' in request.url:
            image_name = ''.join((designation, '.jpg'))
        else:
            image_name = request.url.split('/')[-1]

        image_path = os.path.join(designation_path, image_name)
        return image_path
