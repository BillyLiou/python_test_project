#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import numpy as np
import csv

# 使用np創建陣列
# np1 = np.array([1,2,3])
# np2 = np.array([3,4,5])

# np_t = np1+np2
# print(np_t)
# print(np_t.ndim,np_t.shape,np_t.dtype)

# 讀取csv檔案並操作
# 1.直接讀取
# path = 'test_data.csv'
# try:
#     f = open(path, 'r')
#     rows = csv.reader(f)
#     for row in rows:
#         print(row)
# except:
#     print('Error in reading csv:' + path)
#     exit(1)


# 2. 使用with as 讀取csv檔案

path = 'test_data.csv'
with open(path,encoding='utf-8-sig') as csvfile:
    rows = csv.reader(csvfile)
    filename = next(csvfile).split(',')
    
    # print(filename)
    for row in rows:
        # print(row)
        dic = dict(zip(filename,row))
        print(dic)
# 3. combine two lists into a dictionary



# npd = np.genfromtxt('test_data.csv', delimiter=',',skip_header=1)
# print(npd)
