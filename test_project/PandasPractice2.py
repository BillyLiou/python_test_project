#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import pandas as pd
import numpy as np

test_dict = {
    'white_wine': [1,2,3],
    'red_wine': [3,7,8],
    'cup_cost': [10,5,8]
}

sales = pd.DataFrame(test_dict,index=['Billy','Charly','Tim'])
print(sales)
print(sales.shape)  # 可以獲得回row*column的一個tuple以此為例就是3rows*2columns
print(sales.size) # 可以獲得總共有多少個數
print(sales.head(n=1)) # 可以獲得頭幾筆的資料
print('===========================pandas.DataFrame.info()===========================')
print(sales.info()) # 可以獲得表單資訊
print('======================================================')

# sales.loc['Billy']
print(sales.loc['Billy'])
print(sales.iloc[0:2])

# pandas column
print(sales.columns)
print(sales['white_wine'])
print(sales['white_wine'].shape)
print(sales['red_wine'].head(n=2))

# pandas .loc for more use way

print('======= pandas .loc more use way =======')
print(sales.loc['Billy', 'red_wine':'cup_cost'].head(n=2))



# plus np.array

# list1 = [1,2,3]
# iloc_arr = np.array((0,2))
# # iloc_arr2 = np.array([0,2])
# bool_arr = np.full(3,False,dtype=bool)
# bool_arr[iloc_arr] = True

# print(iloc_arr)
# print(sales.iloc[bool_arr])