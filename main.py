#!/usr/bin/python
from scrapy import cmdline
#cmdline.execute('scrapy crawl AutohomeKoubei -o koubei.csv -t csv'.split())
#cmdline.execute('scrapy crawl spiderb30bbs '.split())
#－o 代表输出文件 －t 代表文件格式

cmdline.execute('scrapy crawl dmoz '.split())