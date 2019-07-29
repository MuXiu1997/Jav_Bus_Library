from scrapy import cmdline

CMD = ['scrapy', 'crawl', 'star_spider']  # 按演员搜索

if __name__ == '__main__':
    cmdline.execute(CMD)
