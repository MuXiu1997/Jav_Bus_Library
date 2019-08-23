from docker_container import DockerContainer

jbl_redis = DockerContainer('redis:5.0.5', name='JBL_redis')
jbl_redis.d() \
    .p(6379, 6379) \
    .v('/JBL/Config/redis.conf', '/usr/local/etc/redis/redis.conf') \
    .v('/JBL/data', '/data') \
    .cmd('redis-server /usr/local/etc/redis/redis.conf')

jbl_gin = DockerContainer('centos:7', name='JBL_gin')
jbl_gin.d() \
    .p(5000, 5000) \
    .v('/JBL/Deploy/Back_end', '/app/Back_end') \
    .cmd('/app/Back_end')


jbl_nginx = DockerContainer('nginx:1.16', name='JBL_nginx')
jbl_nginx.d() \
    .p(80, 80) \
    .v('/JBL/Deploy/Front_end', '/app/html') \
    .v('/JBL/Config/nginx.conf', '/etc/nginx/nginx.conf') \
    .v('/JBL/Deploy/images', '/app/images')

jbl_scrapy = DockerContainer('jbl_scrapy:latest', name='JBL_scrapy')
jbl_scrapy.i().t() \
    .v('/JBL/Crawler_Scrapy/jav_bus_spider_scrapy', '/app/jav_bus_spider_scrapy') \
    .v('/JBL/Crawler_Scrapy/main.py', '/app/main.py') \
    .v('/JBL/Crawler_Scrapy/scrapy.cfg', '/app/scrapy.cfg') \
    .v('/JBL/Deploy/images', '/images')
