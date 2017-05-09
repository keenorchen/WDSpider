#!/usr/bin/env python3

from spider import url_manager, downloader, parser, outputer
from datetime import datetime
from sys import argv


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = downloader.Downloader()
        self.parser = parser.Parser()
        self.outputer = outputer.Outputer()

    def craw(self, url):
        json = self.downloader.download_json(url_wdzj, form_data)
        data_list = self.parser.parse_json(json)

        html = self.downloader.download_html(url_wdty)
        data_list2 = self.parser.parse_html(html)

        self.outputer.collect_data(data_list, data_list2)
        self.outputer.output_json(date_str)


# 程序入口
if __name__ == '__main__':

    # 网贷之家URL
    url_wdzj = "http://shuju.wdzj.com/plat-data-custom.html/"
    date_str = datetime.now().strftime('%Y-%m-%d')
    date_str += date_str
    form_data = {'type': '0',
                 'shujuDate': date_str
                 }

    # 网贷天眼URL
    url_wdty = "http://www.p2peye.com/shuju/ptsj/"
    obj_spider = SpiderMain()
    obj_spider.craw(url_wdzj)
