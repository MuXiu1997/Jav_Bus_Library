from docker_container import DockerContainer

jbl_redis = DockerContainer('redis:5.0.5', name='JBL_redis')
jbl_redis.d() \
    .p(6379, 6379) \
    .v('/JBL/Config/redis.conf', '/usr/local/etc/redis/redis.conf') \
    .v('/JBL/data', '/data') \
    .cmd('redis-server /usr/local/etc/redis/redis.conf')

jbl_flask_gunicorn = DockerContainer('jbl_flask_gunicorn:latest', name='JBL_flask_gunicorn')
jbl_flask_gunicorn.d() \
    .p(5000, 5000) \
    .v('/JBL/Back_end_Flask/manage.py', '/app/manage.py') \
    .v('/JBL/Back_end_Flask/app', '/app/app') \
    .v('/JBL/Config/gunicorn_conf.py', '/app/gunicorn_conf.py') \
    .cmd('gunicorn -c gunicorn_conf.py manage:app')

jbl_nginx = DockerContainer('nginx:1.16', name='JBL_nginx')
jbl_nginx.d() \
    .p(80, 80) \
    .v('/JBL/Front_end_Vue', '/app/html') \
    .v('/JBL/Config/nginx.conf', '/etc/nginx/nginx.conf') \
    .v('/JBL/images', '/app/images')

jbl_scrapy = DockerContainer('jbl_scrapy:latest', name='JBL_scrapy')
jbl_scrapy.i().t() \
    .v('/JBL/Crawler_Scrapy/jav_bus_spider_scrapy', '/app/jav_bus_spider_scrapy') \
    .v('/JBL/Crawler_Scrapy/main.py', '/app/main.py') \
    .v('/JBL/Crawler_Scrapy/scrapy.cfg', '/app/scrapy.cfg') \
    .v('/JBL/images', '/images')
