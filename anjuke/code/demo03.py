#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<>

from requests import *
import re



# 定义一个首页信息类
class MainPageInfo:
    def __init__(self):
        self.url = "http://jy.cmu.edu.cn/module/getonlines?start=0&count=16&k=&professionals=&recruit_type=&degree="
        resp = get(self.url)
        self.resp = resp.content.decode("utf-8")

    def get_page_title(self):
        # 获取每页的标题
        comp = re.findall("\"title\":\"(.*?)\"", self.resp)
        return comp

    def get_zhaopin_type(self):
        # 获取招聘类型
        comp = re.findall("\"recruit_type\":\"(.*?)\"", self.resp)
        return comp

    def get_create_time(self):
        # 获取创建时间
        comp = re.findall("\"create_time\":\"(.*?)\"", self.resp)
        return comp


    def get_main_page_link(self):
        url = "http://www.hrbmu.edu.cn/zsjyc/zpzc/zpxx.htm"
        resp = get(url)
        resp = resp.content.decode("utf-8")

        # 获取每页的链接
        comp = re.findall("class=\"c51631\" href=\"(.*?)\"", resp)
        resp2 = []
        for i in comp:
            i = "http://www.hrbmu.edu.cn/zsjyc/" + i[3:]
            resp2.append(i)
        print("---------------------------------------")
        print(resp2)
        print("---------------------------------------")
        return resp2


def get_single_page_html(url):
    resp = get(url)
    resp = resp.content.decode("utf-8")
    return resp

class ReFind:
    def __init__(self,txt):
        self.txt = txt

    def get_mobile_num(self):
        # patt = "\D(1\d{10})\D"
        # 手机号正则
        patt = "\D(1[35678]\d{9})\D"
        res = re.findall(patt,self.txt)
        return res

    def get_tel_num(self):
        # patt = "\D(1\d{10})\D"
        # 座机号正则
        patt = r'\(?0\d{2,3}[)-]?\d{7,8}'
        res = re.findall(patt, self.txt)
        return res
        pass

if __name__ == '__main__':

    # 构造电话号列表
    tel_num_list = []

    m = MainPageInfo()
    comp = m.get_main_page_link()
    print("-----------首页页面抓取成功-----------")
    print("共抓取到:",len(comp),"条数据")
    j = 0
    for i in comp:
        curr_page_num = []
        j += 1
        print("--------------正在爬取第%d页--------------"%j)
        resp = get_single_page_html(i)
        
        rf = ReFind(resp)
        res = rf.get_mobile_num()
        for i in res:
            # print(i)
            curr_page_num.append(i)
        
        res2 = rf.get_tel_num()
        for i in res2:
            # 要是有中间的横杠杠,
            if i[4] == '-':
                # 啥也不干,
                pass
            else:
                # 否则加上
                i = i[0:4]+'-'+i[4:]
            # print(i)
            curr_page_num.append(i)
        tel_num_list.append(curr_page_num)
    tel_num_list.append([""])
    tel_num_list.append([""])
    tel_num_list.append([""])
    tel_num_list.append([""])
    tel_num_list.append([""])
    tel_num_list.append([""])

    title = m.get_page_title()
    zhao_type = m.get_zhaopin_type()
    create_time = m.get_create_time()

    # for i in title:
    #     print(i)
    #
    # for i in zhao_type:
    #     print(i)
    #
    # for i in create_time:
    #     print(i)
    #
    # for i in tel_num_list:
    #     print(i)

    data = {}
    for i in range(1,len(title)):
        curr_data = [title[i],create_time[i],zhao_type[i]]
        for num in tel_num_list[i]:
            curr_data.append(num)
        data[i] = curr_data

    print(data)

    save_data_to_xls("biao1",data)
