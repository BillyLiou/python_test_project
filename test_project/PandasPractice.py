#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import pandas as pd
import sys
from enum import Enum
from random import randrange

# try:
#     color = sys.stdout
# except AttributeError:
#     raise RuntimeError('runtime error')

# test_dict = {
#     'white_wine': [1,2,3],
#     'red_wine': [3,7,8]
# }

# sales =pd.DataFrame(test_dict,index=['Billy','Charly','Tim'])
# print(sales)
# print(sales.shape)  # 可以獲得回row*column的一個tuple以此為例就是3rows*2columns
# print(sales.size) # 可以獲得總共有多少個數
# print(sales.head(n=1)) # 可以獲得頭幾筆的資料
# print('===========================pandas.DataFrame.info()===========================')
# print(sales.info()) # 可以獲得表單資訊
# print('======================================================')

# cars = ["BMW", "BENZ", "Toyota", "Nissan", "Lexus"]
# selects = pd.Series(cars)
# print(selects)

# dict_city = {
#     "台北": "1",
#     "桃園": "2",
#     "台中": "3",
#     "台南": "4",
#     "高雄": "5", 
# }
# df_city = pd.Series(dict_city,index=dict_city.keys())
# print(df_city)
# print(df_city[[0,2,4]])
# print(df_city[0:2])


# DataFrame範例
# dict_orderId = ['001','002','005','006']
# shop = ['shopA','shopB','','shopC']

# res = {
#     "ID": dict_orderId,
#     "Store": shop
# }

# df = pd.DataFrame(res)
# print(df)

# # DataFrame另一個範例去合併重複的
# amount = [150,200,300]
# store = ['ShopA','ShopB','ShopB']

# store_res = {
#     'Store': store,
#     'Amount': amount
# }

# # 此範例可以將重複的值以加總的方式整合成表格的內容
# store_res = pd.DataFrame(store_res).groupby(['Store']).sum().reset_index()
# print(store_res)

# 此範例為三層式結構時如何分析
data = {
    # 'year':[2012,2013,2013,2015,2015,2016,2015],
    'city': ['A','A','B','C','D','D','A'],
    'amount': [100,300,200,500,400,150,230]
}

city_df = pd.DataFrame(data)
# 以下為依照amount升冪排列,也可以依照別的欄位排列
print(city_df.sort_values(by='amount',ascending=False))


def printData(teststr: str):
    """
    : param teststr:
    這裡可以描述一個function裡面的功能及使用情境
    
    可以print出data有哪些
    
    """
    
    print(teststr)

printData()
# printData('Data is {}'.format(123))



# city_df_1 = city_df['city'].value_counts().rename_axis('city').reset_index(name='counts')

# print(city_df)
# print(city_df_1)


# 這是隨機生成10個隨機年份、直轄市、及銷售金額的程式碼
# YEAR = [2012,2013,2014,2015,2016,2017]
# CITY = ['Taipei','Taoyuang','Taichung','Tainan','Kaohsiung']


# list_res = []
# for i in range(10):
#     tmp_list = [
#         YEAR[randrange(len(YEAR))],
#         CITY[randrange((len(CITY)))],
#         randrange(2000)
#     ]
#     list_res.append(tmp_list)

# city_original = pd.DataFrame(list_res,columns=['Year','City','Amount'])
# city_citycount = city_original.groupby(['Year','City'],as_index=False)['City'].agg({'Count':'count'})
# city_df = pd.DataFrame(list_res,columns=['Year','City','Amount']).groupby(['Year','City']).sum()

# print(city_original)
# print(city_citycount)
# print(city_df)
    
    




