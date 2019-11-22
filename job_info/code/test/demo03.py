# 本模块的功能:<获取每个学习的首页的信息>
from re import findall, I, search
from requests import *
from xlwt import *
from os import path


# 定义一个保存数据函数
def save_data_to_xls(filename, data_list):
    '''
    用于保存数据到表格
    :param filename: 文件名
    :param data: 字典类型数据
    :return:
    '''
    # 需要xlwt库的支持
    # import xlwt
    file = Workbook(encoding='utf-8')
    sheet_name = 0
    for data in data_list:
        sheet_name += 1
        # 指定file以utf-8的格式打开
        table = file.add_sheet('sheet'+str(sheet_name))
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

    # 判断文件存在不
    if path.exists(filename + '.xls'):
        print("保存异常,该文件已经存在!")
    else:
        file.save(filename + '.xls')
        print("-" * 80)
        print("保存数据成功--->", filename)
        print("-" * 80)


file_name = 'test'
data_list = []
for i in range(10):

    data = {
        1: ['首都医学院', '1330206059', '13567542345', '400-88884839', '400-56781235'],
        2: ['首医学院', '1930206059', '135672345', '400-88884839', '400-56781235'],
        3: ['首都学院', '1930206059', '13567542345', '400-4839', '400-56781235'],
        4: ['首都医院', '13930206059', '13567542345', '400-88884839', '400781235']
    }
    data_list.append(data)
save_data_to_xls(file_name, data_list)
