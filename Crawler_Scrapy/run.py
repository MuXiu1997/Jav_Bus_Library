import argparse
import os
import sys
from scrapy import cmdline

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 将当前文件所在目录路径添加到模块搜索路径

parser = argparse.ArgumentParser(description='')
parser.add_argument('--mode', type=str, default='star')
parser.add_argument('--d', type=int, default=0)
args = parser.parse_args()

DELAY = args.d

ALLOWED_DOMAINS = ['dmmsee.men']

API_URL = 'https://www.dmmsee.men/ajax/uncledatoolsbyajax.php?gid={gid}&lang=zh&img={img}&uc={uc}&floor={floor}'

IMAGES_STORE = '/images/'

ALL_START_URLS = ['https://www.dmmsee.men/page/1']

STAR_START_URLS = [
    'https://www.dmmsee.men/star/r62',  # 桜空もも
    'https://www.dmmsee.men/star/okq',  # 三上悠亜
    'https://www.dmmsee.men/star/pmv',  # 橋本ありな
    'https://www.dmmsee.men/star/1ny',  # 明日花キララ
    'https://www.dmmsee.men/star/n5q',  # 天使もえ
    'https://www.dmmsee.men/star/b64',  # 鈴村あいり
    'https://www.dmmsee.men/star/2mx',  # Rio（柚木ティナ）
    'https://www.dmmsee.men/star/mk0',  # 桃谷エリカ
]

TEST_START_URLS = ['https://www.seedmm.co/VEC-357']

CMD = ['scrapy', 'crawl', 'jav_bus_spider']  # 按页搜索

START_URLS = []

if args.mode == 'all':
    START_URLS = ALL_START_URLS
elif args.mode == 'test':
    START_URLS = TEST_START_URLS
else:  # 除'all'与'test'之外的情况都默认为'star'
    START_URLS = STAR_START_URLS
    CMD = ['scrapy', 'crawl', 'star_spider']  # 按演员搜索

if __name__ == '__main__':

    cmdline.execute(CMD)
