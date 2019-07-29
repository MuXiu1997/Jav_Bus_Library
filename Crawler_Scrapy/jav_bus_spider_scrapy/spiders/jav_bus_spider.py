# -*- coding: utf-8 -*-
import random
import re

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jav_bus_spider_scrapy.items import JavSpiderByScrapyItem, JavSpiderByScrapyImagesItem
from jav_bus_spider_scrapy.settings import STAR_LIST, ALLOWED_DOMAINS, API_URL


class JavBusSpiderSpider(CrawlSpider):
    name = 'jav_bus_spider'
    allowed_domains = [ALLOWED_DOMAINS]
    api_url = API_URL

    start_urls = ['https://www.dmmsee.men/page/1']
    rules = (
        Rule(LinkExtractor(allow=r'page/\d$'), follow=True),
        Rule(LinkExtractor(allow=r'.+-.+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # 封面图
        big_image = response.xpath("//a[@class='bigImage']/@href").getall()
        # 预览图
        sample_waterfall = response.xpath("//div[@id='sample-waterfall']/a/@href").getall()
        # 封面图加预览图，用以发送图片下载请求
        image_urls = big_image + sample_waterfall
        # 预览图文件名列表
        sample_list = [sample.split('/')[-1] for sample in sample_waterfall]
        # 番号
        designation = response.xpath("//div[@class='col-md-3 info']/p[1]/span[2]/text()").get()
        # 番名
        designation_title = response.xpath("//a[@class='bigImage']/img/@title").get()
        # 上市时间
        publish_time = response.xpath("//div[@class='col-md-3 info']/p[2]/text()").get()
        # 演出者
        star_name_list = response.xpath("//div[@class='star-name']/a/text()").getall()
        star_name = '、'.join(star_name_list) if star_name_list else "暫無出演者資訊"

        # 使用图片下载管道下载图片
        item = JavSpiderByScrapyImagesItem(
            image_urls=image_urls,
            designation=designation
        )

        yield item

        # script = response.xpath("//body/script/text()").getall()
        # # 遍历得到的列表
        # gid, img, uc, meta = None, None, None, None
        # for each_script in script:
        #     # 如果三个词都在某个标签体中
        #     if "gid" in each_script and "img" in each_script and "uc" in each_script:
        #         # 提取有效信息
        #         gid = re.search(r'gid = (\S+);', each_script).group(1)
        #         img = re.search(r"img = '(\S+)';", each_script).group(1)
        #         uc = re.search(r'uc = (\S+);', each_script).group(1)
        #         # 返回有效信息组成的字典
        #         meta = {
        #             'designation': designation,
        #             'designation_title': designation_title,
        #             'publish_time': publish_time,
        #             'star_name': star_name,
        #             'sample_count': len(sample_waterfall),
        #             'sample_list': sample_list
        #         }
        #         break
        gid, uc, img = re.search(
            r'<script>\s+?var gid = (.*?);\s+?var uc = (.*?);\s+?var img = \'(.*?)\';\s+?</script>',
            response.text
        ).groups()
        meta = {
            'designation': designation,
            'designation_title': designation_title,
            'publish_time': publish_time,
            'star_name': star_name,
            'sample_list': sample_list
        }
        yield Request(
            self.api_url.format(host=ALLOWED_DOMAINS, gid=gid, img=img, uc=uc, floor=random.randint(1, 1000)),
            callback=self.parse_api,
            meta=meta,
            headers={
                'referer': 'https://www.{}/{}'.format(ALLOWED_DOMAINS, designation),
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/74.0.3729.131 Safari/537.36'
            }
        )

    @staticmethod
    def parse_api(response):
        magnet_list = response.xpath("//tr")[1:]
        magnet_infos = []
        for magnet in magnet_list:
            magnet_info = {
                'name': magnet.xpath("./td[1]/a[1]/text()").get().strip(),
                'size': magnet.xpath("./td[2]/a[1]/text()").get().strip(),
                'time': magnet.xpath("./td[3]/a[1]/text()").get().strip(),
                'link': magnet.xpath("./td[1]/a[1]/@href").get()
            }
            magnet_infos.append(magnet_info)

        item = JavSpiderByScrapyItem(
            designation=response.meta.get('designation'),
            designation_title=response.meta.get('designation_title'),
            publish_time=response.meta.get('publish_time'),
            star_name=response.meta.get('star_name'),
            magnet_infos=magnet_infos,
            sample_list=response.meta.get('sample_list'),
        )
        yield item


class JBStarSpider(JavBusSpiderSpider):
    # 继承自按页查询的爬虫，重写部分属性、方法
    name = 'star_spider'
    start_urls = ['https://www.{host}/star/{star}'.format(host=ALLOWED_DOMAINS, star=star) for star in STAR_LIST]
    rules = (
        Rule(LinkExtractor(allow=r'star/.+?/\d+$'), follow=True),
        Rule(LinkExtractor(allow=r'.+-.+'), callback='parse_item', follow=False)
    )
    cookie = {"existmag": "all",
              " __cfduid": "d15e9b022706b222e4ff027d641edc17b1560240493",
              " PHPSESSID": "iaith0urte41vt3qogubcj2v93"}
    headers = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",

        'Cache-Control': "no-cache",
        'Postman-Token': "9d317117-853f-4fac-a1b8-46eff9424aae,2907804a-9242-470c-ae54-7c93377c75b0",
        'Host': "www.{}".format(ALLOWED_DOMAINS),
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, cookies=self.cookie, headers=self.headers, dont_filter=True)
