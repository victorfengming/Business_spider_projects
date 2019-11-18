# -*-coding:utf-8-*-
# 爬取大众点评评论
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')
from contest import *

data_dict = {

}


def filter_time(timestr):
    try:
        timestr = re.search('(\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2})', timestr).group(1)
    except Exception, e:
        print(e)
    return timestr


# 第一步，获得 css url
def get_css_url(html):
    # 获取css文件的内容
    regex = re.compile(r'(s3plus\.meituan\.net.*?)\"')
    css_url = re.search(regex, html).group(0)
    css_url = 'http://' + css_url
    return css_url


def content_replace(content):
    content_list = re.findall('<svgmtsi class="review">(.*?);</svgmtsi>', content)
    content_list_l = []
    for item in content_list:
        item = item.replace("&#x", "uni")
        content_list_l.append(data_dict[item])
    content_list_l = content_list_l + ["</div>"]
    content_end_list = content.split('<svgmtsi')
    content_end = []
    j = 0

    for i in content_end_list:
        content_end.append(i + content_list_l[j])
        j = j + 1

    content_end_str = ''.join(content_end)

    def replace_review(newline):
        newline = str(newline).replace('</div>', "").replace(' ', "")
        re_comment = re.compile('class="review">[^>]*</svgmtsi>')
        newlines = re_comment.sub('', newline)
        newlines = newlines.replace('class="review">', '').replace('</svgmtsi>', '')
        return newlines

    content_end_str = replace_review(content_end_str)

    return content_end_str


def dzdp_conent_spider(item, cookies):
    addr = item['addr']

    shop_id = addr.split('/')[-1]
    print
    shop_id

    for page in range(1, 3):

        url = "http://www.dianping.com/shop/" + shop_id + "/review_all/p" + str(
            page) + "?queryType=sortType&queryVal=latest"
        print
        url

        headers = {

            "Host": "www.dianping.com",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": user_agents,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "http://www.dianping.com/shop/508453/review_all?queryType=sortType&&queryVal=latest",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": cookies,
        }

        # 请求封装方法
        def requests_download(request_max=101):

            result_html = ""
            result_status_code = ""
            try:
                # proxies = get_proxies()
                result = session.get(url=url, headers=headers, verify=False, timeout=20)
                result_html = result.content
                result_status_code = result.status_code

                if result_status_code != 200:
                    result = session.get(url=url, headers=headers, verify=False, timeout=20)
                    result_html = result.content
                    result_status_code = result.status_code
            except Exception as e:
                if request_max > 0:
                    if result_status_code != 200:
                        time.sleep(2)
                        return requests_download(request_max - 1)
            return result_html

        # 调用 requests_download 方法
        a = 2

        result = requests_download(request_max=11)
        result_replace = replace(result)
        result_replace = result_replace.replace('  ', '').replace('  ', "").replace('  ', "").replace('  ', "")
        if '暂无点评' in result_replace or '抱歉！页面无法访问......' in result_replace:
            a = 1
        else:
            result_replaces = \
            re.findall('<div class="reviews-items">(.*?)<div class="bottom-area clearfix">', result_replace)[0]

        if a == 1:
            pass
        else:
            resultList = re.findall('<li>.*?<a class="dper-photo-aside(.*?)>投诉</a>.*?</li>', result_replaces)

            for data in resultList:
                data = str(data)

                try:
                    username = \
                    re.findall('data-click-name="用户名.*?data-click-title="文字".*?>(.*?)<img class=".*?" src=', data)[0]
                except:
                    username = re.findall(
                        'data-click-name="用户名.*?"<br/> data-click-title="文字"<br/>>(.*?)<div class="review-rank"><br/>',
                        data)[0]

                userid = re.findall(' data-user-id="(.*?)".*?data-click-name="用户头像', data)[0]
                headimg = re.findall('<img data-lazyload="(.*?)<div class="main-review">', data)[0]

                try:
                    comment_star = \
                    re.findall('<span class="sml-rank-stars sml-str(.*?) star">.*?<span class="score">', data)[0]
                except:
                    try:
                        comment_star = re.findall(
                            '<span class="sml-rank-stars sml-str(.*?) star">.*?</div>.*?<div class="review-truncated-words">',
                            data)[0]
                    except:
                        comment_star = re.findall(
                            '<span class="sml-rank-stars sml-str(.*?) star"></span>.*?<div class="review-words">',
                            data)[0]

                if '展开评论' in data:
                    content = re.findall('<div class="review-words Hide">(.*?)<div class="less-words">', data)[0]
                else:
                    try:
                        content = re.findall('<div class="review-words">(.*?)<div class="review-pictures">', data)[0]
                    except:
                        content = re.findall('<div class="review-words">(.*?)<div class="misc-info clearfix">', data)[0]

                comment_time = re.findall('<span class="time">(.*?)<span class="shop">', data)[0]
                website = "大众点评"
                pingtai = re.findall('<h1 class="shop-name">(.*?)</h1>.*?<div class="rank-info">', result_replace)[0]

                username = replace_tag(username)
                userid = replace_tag(userid)
                headimg = replace_tag(headimg)
                headimg = headimg.replace('', '')
                comment_star = replace_tag(comment_star)
                comment_star = comment_star.replace('0', "")

                comment_time = replace_tag(comment_time)
                website = replace_tag(website)
                pingtai = replace_tag(pingtai)

                # 爬虫有字体库反爬虫和css映射两种情况

                # 如果是字体库反爬虫，调用 content_replace 方法，修改  data_dict里面的数据，做数据映射 格式 如 'unie02f': '值',
                # content = content_replace(content)

                # svg 格式是 <text x="0" y=  导入 svgutil_3 的 svg2word方法
                # svg 格式是 <path id=".*?" d="M0(.*?)H600  导入 svgutil_4 的 svg2word方法

                from svgutil_4 import svg2word
                css_url = get_css_url(result_replace)

                if '</svgmtsi>' in content:
                    content = svg2word(content, css_url)
                else:
                    content = content
                content = content.replace('<br/>', "")
                print
                content
                crawl_time = str(datetime.now().strftime('%Y-%m-%d %H:%M'))

                comment_time = comment_time[:10] + " " + comment_time[10:]
                comment_time = filter_time(comment_time)
                content = replace_tag(content)

                result_dict = {

                    "username": username,
                    "headimg": headimg,
                    "comment_start": comment_star,
                    "content": content,
                    "comment_time": comment_time,
                    "website": website,
                    "pingtai": pingtai,
                    "crawl_time": crawl_time,

                }

                # 插入MySQL中去
                dbName = "TM_commentinfo_shanghaikeji"
                insert_data(dbName, result_dict)


if __name__ == "__main__":

    cookies = "ctu=e14b301a513cb5e6cb4368ec1a6ef38e098827bd2b05c3a6a03ff7d0ead834f3; _lxsdk_cuid=16c4081aba9c8-018c6bfcb5c785-5f1d3a17-13c680-16c4081aba9c8; _lxsdk=16c4081aba9c8-018c6bfcb5c785-5f1d3a17-13c680-16c4081aba9c8; _hc.v=0d426222-8f95-4389-68ab-d202b3b51e9b.1564450337; __utma=1.1294718334.1564531914.1564531914.1564531914.1; __utmz=1.1564531914.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cy=2; cye=beijing; s_ViewType=10; Hm_lvt_e6f449471d3527d58c46e24efb4c343e=1566184043; aburl=1; Hm_lvt_dbeeb675516927da776beeb1d9802bd4=1566463021; _dp.ac.v=236e82c8-26e1-4496-95f0-9d8b7ba8ca1e; dper=a7fba89f38fb1047d3d06b33821d73e96c141c23a8a6a4a39e746932f07c92067950e08465aaede7532242b58ae779a0dacc3a24f475f1b7b95c4b8cff4b1299e360f5cdab6d77cb939a78f478c0b4e73b6ef56f3deeff682210e5c0fbb428f2; ll=7fd06e815b796be3df069dec7836c3df; ua=%E9%B9%8F; uamo=13683227400; _lxsdk_s=16ce04e6382-9de-106-562%7C%7C155"

    result_list = [
        {"addr": "http://www.dianping.com/shop/22289267"},
        {"addr": "http://www.dianping.com/shop/17951321"},
    ]
    for item in result_list[1:]:
        print("正在采集的位置是：", result_list.index(item))

        dzdp_conent_spider(item, cookies)