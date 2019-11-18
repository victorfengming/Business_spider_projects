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
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'cy=18; cye=shenyang; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=16e790e79f8c8-038d795d750a27-7711a3e-1fa400-16e790e79f8c8; _lxsdk=16e790e79f8c8-038d795d750a27-7711a3e-1fa400-16e790e79f8c8; _hc.v=4deccfc7-5e47-90b6-4e04-c4fa5f04fa52.1573989023; ll=7fd06e815b796be3df069dec7836c3df; ua=%E6%B8%85%E6%99%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E7%BC%95%E9%98%B3%E5%85%89; ctu=db66980f435a78ed85b78178324c2e61fe832ac34177aa8fdacf19f749dc1117; s_ViewType=10; thirdtoken=76c6e023-6f63-4eac-90d3-6cfcbe3ff12a; dper=787e722a04789af45b427ca35bbec771d76f3b78773e9b1294c81ac165cff04b71d0a91e2412d59cf201a5f4ea41aeb1d49e9a5afadbec3582d6bc0d26bc7419dc6a26deb0bb024ebeb2f48ae4368c4ce29bf89b836e0cbc0c38f78b25e603b5; ctu=d09433293c3bad3067253b9217562008b3dfffe7ea09bec37bded498f9e69e2f9efaa9785dafcffdb97b88d2b148fce2; _lxsdk_s=16e7c51b7e3-a5-32b-36c%7C%7C124',
            'Host': 'www.dianping.com',
            'Referer': 'https://graph.qq.com/oauth2.0/show?which=Login&display=pc&scope=get_user_info%2Cadd_share&response_type=code&redirect_uri=https%3A%2F%2Fwww.dianping.com%2Fauthlogin%3Fft%3D6%26timestamp%3D1574045531986%26sign%3D69d48b09f62f6630d3d8875883201db8%26redir%3Dhttps%253A%252F%252Fwww.dianping.com%252Fsearch%252Fkeyword%252F5%252F10_%2525E5%25258D%252597%2525E4%2525BA%2525AC&state=%EA%8E%9E%E4%B5%A3%E4%BE%8C%EF%A5%B8%EC%AE%9E%EA%92%94%E3%87%AC%E5%9A%BF&client_id=200002',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
        }
        self.request_and_get_response()
    def request_and_get_response(self):
        resp = get(self.url,headers=self.headers)
        with open("list_page.html", 'wb') as f:
            f.write(resp.content)
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
