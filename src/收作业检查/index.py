import os
import re
import sys
import pandas as pd
import numpy


# 批量遍历两份名单 检测缺失
def check():
    path = 'C:\\Users\\admin\\Desktop\\javaEE'
    fileList = os.listdir(path)
    currentpath = os.getcwd()
    os.chdir(path)
    name_list = []
    n = 0
    for fileName in fileList:  # 遍历文件夹中所有文件
        pat1 = ".*?([\u4E00-\u9FA5]+).*?"
        name = re.findall(pat1, fileName)
        name_list.append(''.join(name))
        n += 1

    print(n)
    getdata = pd.read_excel(path + '.xlsx', usecols="A")
    npArray = numpy.array(getdata['姓名'])
    name2_list = npArray.tolist()
    print(name_list)
    set_small = set(name_list)
    set_big = set(name2_list)
    print(set_big - set_small)


# 批量修改文件名 xxx-001.zip => 001 xxx.zip
def changeName():
    path = 'C:\\Users\\admin\\Desktop\\javaEE'
    fileList = os.listdir(path)
    # print("修改前："+str(fileList))

    currentpath = os.getcwd()
    os.chdir(path)
    n = 1
    for fileName in fileList:  # 遍历文件夹中所有文件
        pat1 = ".*?([\u4E00-\u9FA5]+).*?"
        pat2 = "\d+"
        pat3 = "(?<=\.).*?(?=$)"
        id = re.findall(pat2, fileName)
        name = re.findall(pat1, fileName)
        suffix = re.findall(pat3, fileName)
        # print(suffix)
        new_fileName = str(id[0]) + ' ' + name[-1] + '.' + suffix[0]
        os.rename(fileName, new_fileName)  # 文件重新命名
        n += 1

    os.chdir(currentpath)
    sys.stdin.flush()
    print("修改后：" + str(os.listdir(path)))