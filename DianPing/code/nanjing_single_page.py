#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>
# TODO 大众点评详情页:本页面爬取的时候返回了一个python-requests,凉凉
import re
from requests import get
from fake_useragent import UserAgent
class Single_page:
    def __init__(self,url):
        self.url = url
        # 发起请求
        # res = get(url, headers=headers, proxies=proxy, timeout=5)

        self._get_single_page_html()
    def _get_single_page_html(self):
        ua = UserAgent()

        headers = {
            'User-Agent': ua.random
        }
        proxy = {
            'http': '47.75.90.57:80',
            'https': '47.75.90.57:80',
        }
        resp = get(self.url, headers=headers, proxies=proxy, timeout=5)
        resp = resp.content.decode("utf-8")
        self.txt = resp


if __name__ == '__main__':

    # sp = Single_page("http://www.dianping.com/shop/67824544")
    sp = Single_page('https://ttk1907.github.io/')
    print(sp.txt)
