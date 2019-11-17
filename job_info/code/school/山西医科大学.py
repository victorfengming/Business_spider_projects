#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from main.usual_spider import *
# 目标地址
url = "http://job.sxmu.edu.cn/eweb/index.so?type=zpxxSearch&xxlb=5100&nrdm=qzzpxx"
# 基础的url,本站的基础地址,
# 用于拼接获取到的半拉科技的地址前面
base_url = "http://job.sxmu.edu.cn/"
# 正则表达式字典
find_pattern_dict = {
    "title": "class=\"omit\">(.*?)</a",
    "link": "<li onclick=\"javascript:window.location.href='(.*?type=zpxxView&id=.*?)'"
}
# 实例化主页信息类对象
mpi = MainPageInfo(url, base_url, find_pattern_dict)
# 链接列表
link_list = mpi.get_single_page_link()
# 标题列表
title_list = mpi.get_every_title()

for i in title_list:
    print(i)

for i in link_list:
    # 创建一个子页面对象
    print(i)
    # rf = ReFind(i)
    # print("-------------------------正在匹配-----------------------------")
    # print(i)
    # print("-------------------------本页面座机号-------------------------")
    # print(rf.get_tel_num())
    # print("-------------------------本页面手机号-------------------------")
    # print(rf.get_mobile_num())









