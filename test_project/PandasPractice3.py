#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import pandas as pd

test_dict = {
    'white_wine': [1,2,3,4],
    'red_wine': [3,7,8,6],
    'cup_cost': [10,5,8,20]
}


sales = pd.DataFrame(test_dict,index=['Billy','Tim','Charly','John'])
print(sales)

# pandas .mean() / .max() / .min()
print(sales.mean())
print(sales['white_wine'].min()) # output = 1,取white_wine的最小值

# pandas calculate var()-變異數 std()-標準差
# 變異數 = 標準差²

print('========== quantile ==========')
print('變異數:')
print(sales.var())
print('標準差:')
print(sales.std())
print('========== ～搞定～ ==========')

#  pandas quantiles
print('========== quantile ==========')
print(sales['white_wine'].quantile([0.3,0.7,1]))
print(sales.quantile(0.5))
print(sales.median())
print()

# pandas describe() 
print('========== describe ==========')
print(sales.describe())
print()

