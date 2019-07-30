from subprocess import call

call(['docker', 'rm', '-f', 'JBL_scrapy'])
call(['docker', 'run', '-it', '--name', 'JBL_scrapy',
      '-v', '/JBL/Crawler_Scrapy/jav_bus_spider_scrapy:/app/jav_bus_spider_scrapy',
      '-v', '/JBL/Crawler_Scrapy/main.py:/app/main.py',
      '-v', '/JBL/Crawler_Scrapy/scrapy.cfg:/app/scrapy.cfg',
      '-v', '/JBL/images:/images',
      'jbl_scrapy:latest'])
