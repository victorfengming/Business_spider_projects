#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from main.usual_spider import *
from main.info_dict import *

print("------------------------------------------")
curr_college = "成都中医药大学"
print("一共有", len(college_info),"个学校 :")
# 实例化主页信息类对象
print("当前是--->",curr_college)
print("------------------------------------------")
info = college_info[curr_college]
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


    # 创建一个子页面对象
    # rf = ReFind(i)
    # print("-------------------------正在匹配-----------------------------")
    # print(i)
    # print("-------------------------本页面座机号-------------------------")
    # print(rf.get_tel_num())
    # print("-------------------------本页面手机号-------------------------")
    # print(rf.get_mobile_num())