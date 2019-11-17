#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<
# 任务三：从大众点评上爬取：南京市各区地标里店铺的美食爬取：
# 店铺名、具体地址、人均消费、推荐菜、当前点评内容这些信息。>



from utils.usual_spider import *

info = dict()
info["url"] = "http://jszg.jschina.com.cn/19835/"

info["base_url"] = "http://jszg.jschina.com.cn/19835/"
info["find_pattern_dict"] = {
            "title": "<div class=\"datatit\"><a href=\"\..*?\">(.*?)</a>",
            "link": "<div class=\"datatit\"><a href=\"\.(.*?)\">.*?</a>",
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

