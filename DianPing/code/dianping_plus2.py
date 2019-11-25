#!/usr/bin/env python
# coding: utf-8
import time

import requests
import random
from xlwt import Workbook
from os import path, remove

# 定义一个保存数据函数
def save_data_to_xls(filename, data_list):
    '''
    用于保存数据到表格
    :param filename: 文件名
    :param data: 字典类型数据
    :return:null
    '''
    # 需要xlwt库的支持
    # import xlwt
    file = Workbook(encoding='utf-8')
    sheet_name = 0
    for data in data_list:
        sheet_name += 1
        # 指定file以utf-8的格式打开
        table = file.add_sheet('sheet' + str(sheet_name))
        # 指定打开的文件名
        # data = {
        #     "1": ["张三", 150, 120, 100],
        #     "2": ["李四", 90, 99, 95],
        #     "3": ["王五", 60, 66, 68]
        # }
        # 字典数据

        ldata = []
        num = [a for a in data]
        # for循环指定取出key值存入num中
        # num.sort()
        # 字典数据取出后无需，需要先排序
        # print("num",num)
        for x in num:
            # for循环将data字典中的键和值分批的保存在ldata中
            t = [int(x)]
            for a in data[x]:
                t.append(a)
            ldata.append(t)
        # print("ldata",ldata)
        for i, p in enumerate(ldata):
            # 将数据写入文件,i是enumerate()函数返回的序号数
            for j, q in enumerate(p):
                # print i,j,q
                table.write(i, j, q)

    file_path = filename + '.xls'
    # 判断文件存在不
    if path.exists(file_path):
        # 直接就给他删除了,还玩啥
        try:
            remove(file_path)
            print("正在重新该文件!")
            file.save(file_path)
            print("-" * 80)
            print("重写数据成功--->", file_path)
            print("-" * 80)
        except:
            print("该文件已经存在!并且另一个程序正在使用此文件")
            print("请关闭文件重试")
    else:
        file.save(file_path)
        print("-" * 80)
        print("保存数据成功--->", file_path)
        print("-" * 80)


# 先定义一个结果集类
class ResultInfo:
    pass


class GetContent:

    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'cy=18; cye=shenyang; _lxsdk_cuid=16e790e79f8c8-038d795d750a27-7711a3e-1fa400-16e790e79f8c8; _lxsdk=16e790e79f8c8-038d795d750a27-7711a3e-1fa400-16e790e79f8c8; _hc.v=4deccfc7-5e47-90b6-4e04-c4fa5f04fa52.1573989023; ua=%E6%B8%85%E6%99%A8%E7%9A%84%E7%AC%AC%E4%B8%80%E7%BC%95%E9%98%B3%E5%85%89; ctu=db66980f435a78ed85b78178324c2e61fe832ac34177aa8fdacf19f749dc1117; s_ViewType=10; dper=787e722a04789af45b427ca35bbec771100d65f45260b4b21379b34ed72d6f6378646aa5f7f1c27426516142c02f7e2959fa25f3901cb3094a2add257c147b1e8e2e9c3041dbd46215bfddf747281fa6421c65227897530a133f6a3c752a7e5f; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=16ea0b1eff8-e09-b02-e9f%7C%7C65',
        'Host': 'www.dianping.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    }

    # css加密字典
    kv = {
        '&#xed32;': 0,
        'kkkkk': 1,
        '&#xe27d;': 2,
        '&#xea76;': 3,
        '&#xe7f6;': 4,
        '&#xe258;': 5,
        '&#xf2a7;': 6,
        '&#xe431;': 7,
        '&#xe2ef;': 8,
        '&#xe305;': 9,
    }

    def getprice(self, price):
        """
        获取价格,用kv的字典来进行匹配替换
        :param price:
        :return:
        """
        for k in list(self.kv.keys()):
            price = price.replace(k, str(self.kv[k]))
        return price

    # def getint(self):
    #     """
    #     生成一个随机数
    #     :return:
    #     """
    #     return str(random.randint(0, 100000))

    def mget(self, url):
        """
        爬虫第二部,发出请求
        :param url: 代请求页面地址
        :param headers: 请求头相关信息
        :return: 返回请求的响应
        """
        # url = self.url + str(page_num)
        try:
            return requests.get(url, headers=self.headers).content.decode("utf-8")
        except Exception as e:
            print(e)
        return 0


def get_single_info(content):
    """
    用于将content 的内容,替换查找成为想要的内容
    :param content: 爬取到的界面html
    :return: 返回一个装有数据的对象集合
    """
    # 定义结果列表
    info_list = []

    while True:
        # 实例化一个结果集对象
        ri = ResultInfo()

        p1 = content.find("'moduleClick', 'shoppic'")
        if p1 >= 0:
            content = content[p1:]
            p2 = content.find('<img title="')
            p3 = content.find('" alt="')
            shopname = content[p2 + 12:p3]
            # print(shopname)
            # 将信息存储到对象中
            ri.shopname = shopname

            p2 = content.find("<b>")
            tmp = content[p2 + 10:]
            z1 = tmp.find("<b>")
            tmp = tmp[z1:]
            z2 = tmp.find("</b>")
            price = tmp[3:z2].replace('<svgmtsi class="shopNum">', '').replace('</svgmtsi>', '')
            price = GetContent().getprice(price)
            # print(price)
            # 这里也是
            ri.price = price

            p2 = content.find("data-address")
            p3 = content.find("data-sname=")
            address = content[p2 + 14:p3 - 2]
            # print(address)
            # 地址追加进去
            ri.address = address

            p2 = content.find('<div class="recommend">')
            p3 = content.find('<span class="comment-list">')
            tmp = content[p2:p3]
            recommand = []
            while True:
                t1 = tmp.find('_blank')
                if t1 >= 0:
                    t2 = tmp.find("</a>")
                    rec = tmp[t1 + 8:t2]
                    # print(rec)
                    recommand.append(rec)

                    tmp = tmp[t1 + 50:]
                else:
                    break

            # for x in recommand:
            #     print("\t" + x)

            ri.recommand = recommand

            p2 = content.find('<span class="comment-list">')
            p3 = content[p2:].find('</div>')
            tmp = content[p2:p2 + p3]
            # 先定义一个空
            others = []
            while True:
                t1 = tmp.find('<span >')
                if t1 >= 0:
                    t2 = tmp.find("</span>")
                    comm = tmp[t1 + 7:t2]
                    comm = comm.replace('<svgmtsi class="shopNum">', '').replace('</svgmtsi>', '').replace('<b>',
                                                                                                           '').replace(
                        '</b>', '')
                    other = GetContent().getprice(comm)
                    others.append(other)
                    tmp = tmp[t2 + 5:]
                else:
                    break
            # 存入对象中
            ri.kouwei = others[0]
            ri.environment = others[1]
            ri.server = others[2]
            # print("------------------------------------")

            n = content[100:].find("'moduleClick', 'shoppic'")
            content = content[n + 100:]

        else:
            break

        info_list.append(ri)
    return info_list


def save2file(city, curr_url, max_page):
    '''
    保存一个城市的信息
    :param city:
    :param max_page:
    :return:
    '''
    # 设定最大页数
    # max_page = 17
    # 将数据存储到文件中
    data_list = []
    # 文件名
    filename = city
    # 先判断一下有没有这么多页
    max_page = max_page if max_page <= 50 else 50
    # 遍历所有页'
    for page_num in range(1, max_page + 1):

        # 调用get方法获取响应内容
        curr_url = curr_url + str(page_num)
        # print("当前的url是: ",curr_url)
        content = GetContent().mget(curr_url)
        # print(content)
        # 用于存入文件,第一次存入后就不用了
        '''
        content=""
        fp=open("c.txt")
        for x in fp.readlines():
            content=content+x
        #print content
        '''

        # 这里缺了一个转码
        # content = content.decode("utf-8")

        # print(conte|nt)

        info_list = get_single_info(content)

        # data = {
        #     "1": ["张三", 150, 120, 100],
        #     "2": ["李四", 90, 99, 95],
        #     "3": ["王五", 60, 66, 68]
        # }
        data = {

        }
        # print("-" * 60)
        # 定义列一个表头
        num = 0
        # 添加行表头
        head = ['店铺名称', '人均价格', '店铺地址', '推荐菜品1', '推荐菜品2', '推荐菜品3', '口味评分', '环境评分', '服务评分']
        data[num] = head
        # 遍历列表数据
        for info in info_list:
            # 更新
            num += 1
            curr_row = []
            curr_row.append(info.shopname)
            curr_row.append(info.price)
            curr_row.append(info.address)
            # 保证recommend的长度固定
            # 表格列对其
            chang = len(info.recommand)
            for i in range(chang):
                curr_row.append(info.recommand[i])
            for j in range(3 - chang):
                curr_row.append("")

            curr_row.append(info.kouwei[2:])
            curr_row.append(info.environment[2:])
            curr_row.append(info.server[2:])
            '''
            {'shopname': '从你的全世界路过(1912总统府店)', 'price': '￥108', 'address': '太平北路66号南京1912街区A10栋', 'recommand': ['梅茜的午餐', '老情书', '芝士焗红薯'], 'kouwei': '口味7.7', 'environment': '环境8.8', 'server': '服务8.3'}
            '''
            data[num] = curr_row
            # 不用写toString方法也可以打印出对象的所有成员属性的内容
            # python中对象的成员属性可以动态添加,java就不行,完蛋儿
            print(info.__dict__)
        # 将当前sheet数据追加到对象列表中
        data_list.append(data)

    # print("-" * 60)

    # 最终保存数据到文件
    save_data_to_xls(filename, data_list)

#
# city_dict = {
#     '南京': "http://www.dianping.com/nanjing/ch10/p",
#     '北京': 'http://www.dianping.com/beijing/ch10/p',
#     '天津': 'http://www.dianping.com/tianjin/ch10/p'
# }

if __name__ == '__main__':

    # 设置最大页数
    max_page = 1
    print("-"*80)
    print("| 欢迎使用大众点评抓取工具")
    print("-"*80)
    curr_city = input("| 请输入需要抓取的城市名称全拼:")
    print("-"*80)
    url = "http://www.dianping.com/"+curr_city+"/ch10/p"

    while True:
        try:
            max_page = int(input("| 请问需要多少页的数据(1-50):"))
            break
        except:
            print('| 抱歉,您输入有瑕疵,请重新输入!')

    try:
        # print('正在抓取,请稍后...')
        # 保存一个文件
        save2file(curr_city, url, max_page)
    except:
        print("| 系统繁忙,抓取失败!")



