import requests,re,os
from lxml import etree
# url='https://book.douban.com/tag/%E9%9D%92%E6%98%A5%E6%96%87%E5%AD%A6?start=0&type=T'
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
#     }

# with open('./ip.txt','r',encoding='utf-8') as fp:
#     res=fp.readlines()
#     res=[i.rstrip('\n') for i in res]
#     ip=res[2]
# pro={
#     'http':ip,
#     'https':ip
# }
# res=requests.get(url,headers=headers,proxies=pro,timeout=5)
# res.encoding='utf-8'
# with open('./douban_book.html','w',encoding='utf-8') as fp:
#     fp.write(res.text)

# 获取指定数据
with open('./douban_book.txt','r',encoding='utf-8') as fp:
    res=fp.read()

    # print(res)
html=etree.HTML(res)
# print(html)
# 标题
title=html.xpath('//div[@class="info"]/h2/a/text()')
title=[re.sub('\s','',i) for i in title]
for i in title:
    if i=='':
        title.remove(i)



# 摘要
describ=html.xpath('//div[@class="info"]//p/text()')
describ=[re.sub('\s','',i) for i in describ]
# print(describ)

# zz_price=html.xpath('//span[@class="buy-info"]/a/text()')
# zz_price=[re.sub('\s','',i) for i in zz_price]
# print(zz_price)

# 图片
# image=html.xpath('//div[@class="pic"]/a/img/@src')
# imageurl=[re.sub('\s','',i) for i in image]
# print(image)
#下载图片
# for i in imageurl:
#     # print(i)
#     result=requests.get(i)
#     res=i.split('/')
#     imgurl=res[-1]
#     with open(f'./0928_yanzheng_ip/images/{imgurl}','wb') as fp:
#         fp.write(result.content)

res=os.listdir('./0928_yanzheng_ip/images')
# print(res)

q_url='0928_yanzheng_ip\images'
result=[os.path.join(q_url,i)for i in res]
# print(result)

# 作者  出版社  出版年份   价钱
author=html.xpath('//div[@class="pub"]/text()')
author=[re.sub('\s','',i) for i in author]


au=[i.split('/')[0] for i in author]
# print(author)
publisher=[i.split('/')[1] for i in author]
# print(publisher)
createtime=[i.split('/')[2] for i in author]
# print(createtime)
out_price=[i.split('/')[3] for i in author]
# print(out_price)
arr=list(zip(title,result,au,publisher,createtime,out_price,describ))
# print(arr)


import pymysql
def model(sql,arr):

    py=pymysql.connect('127.0.0.1','root','123456789','zy',charset='utf8mb4')
    cursor=py.cursor()
    sql='insert into douban_book values(null,%s,%s,%s,%s,%s,%s,%s)'
    cursor.executemany(sql,arr)
    py.commit()
    py.close()

