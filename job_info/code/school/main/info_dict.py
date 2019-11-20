#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Created by 秋叶夏风

# 本模块的功能:<用于存储各个网站信息>
template1 = {
                "title": "<a href='.*?' target='_blank' title='(.*?)'>",
                "link": "<a href='(.*?)' target='_blank' title='.*?'>",
            },

template2 = {
                "title": "<a href=\"/campus/view/id/.*?\" target=\"_blank\">(.*?)</a>",
                "link": "<a href=\"(/campus/view/id/.*?)\" target=\"_blank\">.*?</a>",
            },

college_info = {

    # TODO 这个在第二条数据卡住了,代解决
    "天津医科大学": {
        # 目标地址
        "url": "http://www.tmu.edu.cn/jyw/3334/list.htm",
        # 基础的url,本站的基础地址,
        # 用于拼接获取到的半拉科技的地址前面
        "base_url": "http://www.tmu.edu.cn/",
        # 正则表达式字典
        "find_pattern_dict": {
            "title": "htm' target='_blank' title='(.*?)'",
            "link": "'(.*?htm)' target='_blank' title="
        },
    },
    "首都医科大学": {
        "url": "http://jy.ccmu.edu.cn/sites/p/01/main.jsp?ColumnID=p_24",
        "base_url": "http://jy.ccmu.edu.cn/",
        "find_pattern_dict": {
            "title": "<a title='(.*?)' href=\"javascript:openUrl\('/p/24/.*?'\)",
            "link": "<a title='.*?' href=\"javascript:openUrl\('/(p/24/.*?)'\)",
        },
    },

    "天津中医药大学": {
        "url": "http://zsjy.tjutcm.edu.cn/list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1013",
        "base_url": "http://zsjy.tjutcm.edu.cn/",
        "find_pattern_dict": {
            "title": "href=\"info.*?\" target=\"_blank\"   title=\"(.*?)\">",
            "link": "href=\"(info.*?)\" target=\"_blank\"   title=\".*?\">",
        },
    },
    "安徽中医药大学": {
        "url": "http://jyxxw.ahtcm.edu.cn/1727/list2.htm",
        "base_url": "http://jyxxw.ahtcm.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href='.*?' target='_blank' title='(.*?)'>",
            "link": "<a href='(.*?)' target='_blank' title='.*?'>",
        },
    },
    "牡丹江医学院": {
        "url": "http://mdjmujy.university-hr.com/showmore.php?actiontype=12&pg=1",
        "base_url": "http://mdjmujy.university-hr.com/",
        "find_pattern_dict": {
            "title": "search_keyword=\" title=\"\">(.*?)</a>",
            "link": "href=\"(.*?search_keyword=)\" title=\"\">.*?</a>",
        },
    },

    "黑龙江中医药大学": {
        "url": "http://zyyjyxx.hljucm.net/zpxx/zpxx.htm",
        "base_url": "http://zyyjyxx.hljucm.net/",
        "find_pattern_dict": {
            "title": "<h3><a href=\".*?\">(.*?)</a></h3>",
            "link": "<h3><a href=\"\.\.(.*?)\">.*?</a></h3>",
        },
    },

    "山西医科大学": {
        "url": "http://job.sxmu.edu.cn/eweb/index.so?type=zpxxSearch&xxlb=5100&nrdm=qzzpxx",
        "base_url": "http://job.sxmu.edu.cn/",
        "find_pattern_dict": {
            "title": "class=\"omit\">(.*?)</a",
            "link": "<li onclick=\"javascript:window.location.href='(.*?type=zpxxView&id=.*?)'"
        },
    },

    "河北医科大学": {
        "url": "http://202.206.48.97:8081/xinwen.aspx?lei=6&sectionid=9",
        "base_url": "http://202.206.48.97:8081/",
        "find_pattern_dict": {
            "title": "text-decoration: none;\">[\s]+\n[\s]+(.*?)\n",
            "link": "href='(RedArt\.aspx\?article_id=.*?)'"
        },
    },

    "沈阳药科大学": {
        "url": "http://syphu.jysd.com/campus",
        "base_url": "http://syphu.jysd.com/",
        "find_pattern_dict": {
            "title": "<a href=\"/campus/view/id/.*?\" target=\"_blank\">(.*?)</a>",
            "link": "<a href=\"(/campus/view/id/.*?)\" target=\"_blank\">.*?</a>",
        },
    },

    "哈尔滨医科大学": {
        "url": "http://www.hrbmu.edu.cn/zsjyc/zpzc/zpxx.htm",
        "base_url": "http://www.hrbmu.edu.cn/zsjyc/",
        "find_pattern_dict": {
            "title": "href=\".*?\" target=\"_blank\" title=\"(.*?)\"",
            "link": "href=\"\.\.(.*?)\" target=\"_blank\" title=\".*?\"",
        },
    },

    "皖南医学院": {
        "url": "http://jiuye.wnmc.edu.cn/_t378/zpxx/list.psp",
        "base_url": "http://jiuye.wnmc.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href='.*?' target='_blank' title='(.*?)'>",
            "link": "<a href='(.*?)' target='_blank' title='.*?'>",
        },
    },
    "蚌埠医学院": {
        "url": "https://xsc.bbmc.edu.cn/jyzdzx/zpxx.htm",
        "base_url": "https://xsc.bbmc.edu.cn/jyzdzx/",
        "find_pattern_dict": {
            "title": "<a href=\"info.*?\" style=\"float:left;\">(.*?)</a>",
            "link": "<a href=\"(info.*?)\" style=\"float:left;\">.*?</a>",
        },
    },

    "赣南医学院": {
        "url": "http://jy.gmu.cn/campus",
        "base_url": "http://jy.gmu.cn/",
        "find_pattern_dict": {
            "title": "<a href=\"/campus/view/id/.*?\" target=\"_blank\">(.*?)</a>",
            "link": "<a href=\"(/campus/view/id/.*?)\" target=\"_blank\">.*?</a>",
        },
    },
    "山东中医药大学": {
        "url": "https://jiuye.sdutcm.edu.cn/031/pagelist.jsp?id=c80a152d39ed4a799d0da2daf546aa7d",
        "base_url": "https://jiuye.sdutcm.edu.cn/",
        "find_pattern_dict": {
            "title": "href=\".*?\" target=_blank>(.*?) </A>",
            "link": "href=\"(/031/content.*?)\" target=_blank>.*? </A>",
        },
    },

    "山东第一医科大学": {
        "url": "http://sa.sdfmu.edu.cn/gzdh1/jyzd1/zpxx.htm",
        "base_url": "http://sa.sdfmu.edu.cn/",

        "find_pattern_dict": {
            "title": "<a href=\".*?\" target=\"_blank\">(.*?)</a>",
            "link": "<a href=\"\.\./\.\.(/info/.*?)\" target=\"_blank\">.*?</a>",
        },
    },

    "济宁医学院": {
        "url": "http://jyzd.jnmc.edu.cn/988/list.htm",
        "base_url": "http://jyzd.jnmc.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href='.*?' target='_blank' title='(.*?)'>",
            "link": "<a href='(.*?)' target='_blank' title='.*?'>",
        },
    },

    "新乡医学院": {
        "url": "http://job.xxmu.edu.cn/campus",
        "base_url": "http://job.xxmu.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href=\"/campus/view/id/.*?\" target=\"_blank\">(.*?)</a>",
            "link": "<a href=\"(/campus/view/id/.*?)\" target=\"_blank\">.*?</a>",
        },
    },

    "湖北中医药大学": {
        "url": "http://hbtcm.91wllm.com/campus",
        "base_url": "http://hbtcm.91wllm.com/",
        "find_pattern_dict": {
            "title": "<a href=\"/campus/view/id/.*?\" target=\"_blank\">(.*?)</a>",
            "link": "<a href=\"(/campus/view/id/.*?)\" target=\"_blank\">.*?</a>",
        },
    },

    "湖北医药学院": {
        "url": "http://hbmu.91wllm.com/teachin",
        "base_url": "http://hbmu.91wllm.com/",
        "find_pattern_dict": {
            "title": "<a href=\"/teachin/view/id/.*?\" title=\"(.*?)\" target=\"_blank\">",
            "link": "<a href=\"(/teachin/view/id/.*?)\" title=\".*?\" target=\"_blank\">",
        },
    },

    "广州医科大学": {
        "url": "https://yjs.gzhmu.edu.cn/jygz.htm",
        "base_url": "https://yjs.gzhmu.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href=\"info/.*?\" title=\"(.*?)\" target=\"_blank\">",
            "link": "<a href=\"(info/.*?)\" title=\".*?\" target=\"_blank\">",
        },
    },

    "广东医科大学": {
        "url": "http://jyzd.gdpu.edu.cn/zpxx1.htm",
        "base_url": "http://jyzd.gdpu.edu.cn/",
        "find_pattern_dict": {
            "title": "<A href=\"info/.*?\">(.*?)</A>",
            "link": "<A href=\"(info/.*?)\">.*?</A>",
        },
    },

    "内蒙古医科大学": {
        "url": "http://immc.university-hr.com/showmore.php?actiontype=8",
        "base_url": "http://immc.university-hr.com/",
        "find_pattern_dict": {
            "title": "<a href=\"showarticle.*?\"[.|\s]*?>(.*?)</a>",
            "link": "<a href=\"(showarticle\.php\?actiontype=8&id=.*?)\"",
        },
    },

    "广西医科大学": {
        "url": "http://jcy.gxmu.edu.cn/nologin/school!articleNewsIndex.htm?article.searchArticleType=24",
        "base_url": "http://jcy.gxmu.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href=\"/nologin/school!articleDetail\.htm\?.*?\" target=\"_blank\">(.*?)</a>",
            "link": "<a href=\"(/nologin/school!articleDetail\.htm\?.*?)\" target=\"_blank\">.*?</a>",
        },
    },

    # TODO 这个返回了404 ,大瑕疵,有待解决
    # "成都中医药大学": {
    #     "url": "http://zsjy.cdutcm.edu.cn/Work/",
    #     "base_url": "http://zsjy.cdutcm.edu.cn/",
    #     "find_pattern_dict": {
    #         "title": "<a href=\"/Work/5467/4099.html\" title=\"智汇天府•四川招聘大会\"",
    #         "link": "<a href=\"(/Work/.*?)\" title=\".*?\"",
    #     },
    # },

    "西南医科大学": {
        "url": "https://jy.swmu.edu.cn/Work/Index/100022",
        "base_url": "https://jy.swmu.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href=\"/Work/.*?\" title=\"(.*?)\" class=\"title\"",
            "link": "<a href=\"(/Work/.*?)\" title=\".*?\" class=\"title\"",
        },
    },

    # TODOE <Response [403]>
    #     "川北医学院": {
    #         "url": "http://career.nsmc.edu.cn/Work",
    #         "base_url": "http://career.nsmc.edu.cn/",
    # "find_pattern_dict": {
    #             "title": "<a href=\"/Work/.*?\" title=\"(.*?)\" class=\"roll",
    #             "link": "<a href=\"(/Work/.*?)\" title=\".*?\" class=\"roll\"",
    #         },
    #     },

    # TODO 后面的字典仍然需要进行完善

    "成都医学院": {
        "url": "http://jy.cmc.edu.cn/search/query.action?partId=3",
        "base_url": "http://jy.cmc.edu.cn/",
        "find_pattern_dict": {
            "title": "<a href=\"/html/zhaopin/.*?\"[.|\s]*?class=\"non-line fnt_333333_13\">(.*?)</a>",
            "link": "<a href=\"(/html/zhaopin/.*?)\"[.|\s]*?class=\"non-line fnt_333333_13\">.*?</a>",
        },
    },


}
