# -*- coding: utf-8 -*-
from container import jbl_redis, jbl_flask_gunicorn, jbl_nginx, jbl_scrapy


def run_server():
    jbl_redis.rerun()
    jbl_flask_gunicorn.rerun()
    jbl_nginx.rerun()


def run_scrapy():
    jbl_scrapy.rerun()


if __name__ == '__main__':
    i = input('1. 重启网站服务器\n2. 启动爬虫容器\n')
    if i == '1' or i == 1:
        run_server()
    elif i == '2' or i == 2:
        run_scrapy()
    else:
        exit()
