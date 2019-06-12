docker rm -f JBL_scrapy

docker run -it --name JBL_scrapy\
 -v /JBL/Crawler_Scrapy/jav_bus_spider_scrapy:/app/jav_bus_spider_scrapy\
 -v /JBL/Crawler_Scrapy/run.py:/app/run.py\
 -v /JBL/Crawler_Scrapy/scrapy.cfg:/app/scrapy.cfg\
 -v /JBL/Models_SQLAlchemy/models.py:/app/models.py\
 -v /JBL/Models_SQLAlchemy/Jav_Bus.db:/app/Jav_Bus.db\
 -v /JBL/images:/images\
 jbl_scrapy:latest

