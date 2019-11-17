#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<获取每个学习的首页的信息>
from re import findall
from requests import *


class MainPageInfo:
    """
    本类用于获取主页面的信息
    比如标题,子页面链接...
    """

    def __init__(self, url, base_url, find_pattern_dict):
        self.url = url
        self.base_url = base_url
        self.find_title_pattern = find_pattern_dict["title"]
        self.find_link_pattern = find_pattern_dict["link"]

        self.request_and_get_response()
    def request_and_get_response(self):
        resp = get(self.url)
        try:
            self.resp = resp.content.decode("utf-8")
        except:
            self.resp = resp.content.decode("gbk")
        print("-----------------------------------------------------------------")
        print(resp)
        print("-----------------------------------------------------------------")
    def get_single_page_link(self):
        link_list = []
        res = findall(self.find_link_pattern, self.resp)
        for i in res:
            # print(i)
            link_list.append(self.base_url + i)
        return link_list
        pass

    def get_every_title(self):
        every_title = []
        res = findall(self.find_title_pattern, self.resp)
        for i in res:
            # print(i)
            every_title.append(i)
        return every_title
        pass


class ReFind:
    """
    页面内部正则匹配类
    """

    def __init__(self, url):
        self.url = url
        self._get_single_page_html()

    def _get_single_page_html(self):
        resp = get(self.url)
        resp = resp.content.decode("utf-8")
        self.txt = resp

    def get_mobile_num(self):
        # patt = "\D(1\d{10})\D"
        # 手机号正则
        patt = "\D(1[35678]\d{9})\D"
        res = findall(patt, self.txt)
        return res

    def get_tel_num(self):
        # patt = "\D(1\d{10})\D"
        # 座机号正则
        patt = r'\(?0\d{2,3}[)-]?\d{7,8}'
        res = findall(patt, self.txt)
        return res
        pass


if __name__ == '__main__':
    # 目标地址
    url = "http://www.tmu.edu.cn/jyw/3334/list.htm"
    # 基础的url,本站的基础地址,
    # 用于拼接获取到的半拉科技的地址前面
    base_url = "http://www.tmu.edu.cn/"
    # 正则表达式字典
    find_pattern_dict = {
        "title": "htm' target='_blank' title='(.*?)'",
        "link": "'(.*?htm)' target='_blank' title="
    }
    # 实例化主页信息类对象
    mpi = MainPageInfo(url, base_url, find_pattern_dict)
    # 链接列表
    link_list = mpi.get_single_page_link()
    # 标题列表
    title_list = mpi.get_every_title()

    # for i in title_list:


    for i in link_list:
        # 创建一个子页面对象
        rf = ReFind(i)
        print("-------------------------正在匹配-----------------------------")
        print(i)
        print("-------------------------本页面手机号-------------------------")
        print(rf.get_tel_num())
        print("-------------------------本页面座机号-------------------------")
        print(rf.get_mobile_num())
