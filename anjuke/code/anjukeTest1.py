#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<
# 任务一：
# 从安居客网站上：搜索南京市的二手房的面积、售价、小区名、价格、位置
# （要精确到属于哪个区、具体的地址）、是否学区房、装修、这些信息。
# TODO 安居客封锁IP地址,计划解决方案,使用代理ip来进行请求

from usual_spider import *

info = dict()
info["url"] = "https://nanjing.anjuke.com/sale/"
info["base_url"] = ""
info["find_pattern_dict"] = {
            "title": "title=\"(.*?)\" href=\"https://nanjing.anjuke.com/prop/view.*?\" target='_blank' class=\"houseListTitle \">",
            "link": "title=\".*?\" href=\"(https://nanjing.anjuke.com/prop/view.*?)\" target='_blank' class=\"houseListTitle \">",
        }


print(type(info))

mpi = MainPageInfo(info["url"], info["base_url"], info["find_pattern_dict"])
# 标题列表
title_list = mpi.get_every_title()
print("------------------------------------------")
print("标题获取成功")
print("一共有：",len(title_list),"个标题")
print("------------------------------------------")
for i in title_list:
    print(i)

# 链接列表
link_list = mpi.get_single_page_link()
print("------------------------------------------")
print("链接获取成功")
print("一共有：",len(link_list),"个链接")
print("------------------------------------------")

for i in link_list:
    print(i)