#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import pandas as pd

test_dict = {
    'white_wine': [1,2,3],
    'red_wine': [3,7,8]
}

sales =pd.DataFrame(test_dict,index=['Billy','Charly','Tim'])
print(sales)
print(sales.shape)  # 可以獲得回row*column的一個tuple以此為例就是3rows*2columns
print(sales.size) # 可以獲得總共有多少個數
print(sales.head(n=1)) # 可以獲得頭幾筆的資料
print('===========================pandas.DataFrame.info()===========================')
print(sales.info()) # 可以獲得表單資訊
print('======================================================')

