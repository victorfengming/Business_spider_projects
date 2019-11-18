import requests,random
url='https://www.baidu.com/'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }
with open('./xxcc.txt','r',encoding='utf-8') as fp:
    res=fp.readlines()
    res=[i.rstrip('\n') for i in res]
    # print(res)
    ip=random.choice(res)
    # print(res)
    # print(type(res))
pro={
    'http':ip,
    'https':ip
}
try:
    res=requests.get(url,headers=headers,proxies=pro,timeout=5)
    if res.status_code==200:
        with open('./ip.txt','a',encoding='utf-8') as fp:
            fp.write(ip+'\n')
            print('ip是好的')
    else:
        print('ip不好使')
except:
    print('发生错误')



