#!/usr/bin/env python
# coding: utf-8
import requests
import json
import random


def getprice(price):
    for k in kv.keys():
        price = price.replace(k, str(kv[k]))
    return price


def getint():
    return str(random.randint(0, 100000))


def mget(url, headers):
    try:
        return requests.get(url, headers=headers).content
    except Exception, e:
        print e
    return 0


HH = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "text/html;charset=UTF-8",
    "Connection": "keep-alive",
    "Keep-Alive": "timeout=5",
    "Cache-Control": "max-age=0",
    "Cookie": "s_ViewType=10; _lxsdk_cuid=16e9d73c1a377-0783cd8d32352c-e343166-1fa400-16e9d73c1a4c8; _lxsdk=16e9d73c1a377-0783cd8d32352c-e343166-1fa400-16e9d73c1a4c8; _hc.v=4314e0c2-b381-8d7a-acbd-df91892df240.1574599640; _lxsdk_s=16e9db8187a-790-75e-cbb%7C%7C2"
}

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

content = mget("http://www.dianping.com/nanjing/ch10/r1692", HH)
print content
'''
content=""
fp=open("c.txt")
for x in fp.readlines():
    content=content+x
#print content
'''

while True:
    print '循环一次'
    p1 = content.find("'moduleClick', 'shoppic'")
    print p1
    if p1 >= 0:
        content = content[p1:]
        p2 = content.find('<img title="')
        p3 = content.find('" alt="')
        shopname = content[p2 + 12:p3]
        print shopname

        p2 = content.find("<b>")
        tmp = content[p2 + 10:]
        z1 = tmp.find("<b>")
        tmp = tmp[z1:]
        z2 = tmp.find("</b>")
        price = tmp[3:z2].replace('<svgmtsi class="shopNum">', '').replace('</svgmtsi>', '')
        price = getprice(price)
        print price

        p2 = content.find("data-address")
        p3 = content.find("data-sname=")
        address = content[p2 + 14:p3 - 2]
        print address

        p2 = content.find('<div class="recommend">')
        p3 = content.find('<span class="comment-list">')
        tmp = content[p2:p3]
        recommand = []
        while True:
            t1 = tmp.find('_blank')
            if t1 >= 0:
                t2 = tmp.find("</a>")
                rec = tmp[t1 + 8:t2]
                print rec
                recommand.append(rec)
                tmp = tmp[t1 + 50:]
            else:
                break

        for x in recommand:
            print "\t" + x

        p2 = content.find('<span class="comment-list">')
        p3 = content[p2:].find('</div>')
        tmp = content[p2:p2 + p3]
        while True:
            t1 = tmp.find('<span >')
            if t1 >= 0:
                t2 = tmp.find("</span>")
                comm = tmp[t1 + 7:t2]
                comm = comm.replace('<svgmtsi class="shopNum">', '').replace('</svgmtsi>', '').replace('<b>','').replace('</b>', '')
                print getprice(comm)
                tmp = tmp[t2 + 5:]
            else:
                break

        print "------------------------------------"

        n = content[100:].find("'moduleClick', 'shoppic'")
        content = content[n + 100:]


    else:
        print "走的else"
        break





