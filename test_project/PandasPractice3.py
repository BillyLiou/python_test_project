#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   PandasPractice3.py
@Time    :   2021/02/04 15:56:01
@Author  :   Billy Liu
@Version :   1.0
@Contact :   billy@test.mail
@Desc    :   None
'''


import pandas as pd

test_dict = {
    'white_wine': [1,2,3,4],
    'red_wine': [3,7,8,6],
    'cup_cost': [10,5,8,20]
}


sales = pd.DataFrame(test_dict,index=['Billy','Tim','Charly','John'])
print(sales)

# # pandas .mean() / .max() / .min()
# print(sales.mean())
# print(sales['white_wine'].min()) # output = 1,取white_wine的最小值

# # pandas calculate var()-變異數 std()-標準差
# # 變異數 = 標準差²

# print('========== quantile ==========')
# print('變異數:')
# print(sales.var())
# print('標準差:')
# print(sales.std())
# print('========== ～搞定～ ==========')

# #  pandas quantiles
# print('========== quantile ==========')
# print(sales['white_wine'].quantile([0.3,0.7,1]))
# print(sales.quantile(0.5))
# print(sales.median())
# print()

# # pandas describe() 
# print('========== describe ==========')
# print(sales.describe())
# print()

# # pandas iloc()
# print('========== iloc ==========')

# # 應該怎麼記呢,index第幾個的第幾個欄位,
# # 第一個參數是第幾個index也就是0個 = Billy
# # 第二個參數是第幾個欄位也就是1
# print(sales.iloc[0,1])

# # 若想知道前兩個的第一欄位可以有[0:1,1]去找
# print(sales.iloc[0:2,[1]])


# print('========== loc ==========')
# # loc也是一樣的,差別在iloc是以數字(index)作為篩選標準,loc是以行列的title
# # 第一個參數是第幾個index也就是0個 = Billy
# # 第二個參數是第幾個欄位也就是1

# # 先求算出有哪幾個red_wine是大於6的
# print(sales.loc[:,"red_wine"]>6)

# # 列出滿足red_wine大於6的列
# print(sales[sales.loc[:,"red_wine"]>6])
# print()

# # 列出滿足red_wine大於6的那些列但只列出white_wine的數字
# print(sales[sales.loc[:,"red_wine"]>6].loc[:,['white_wine']])


# print('========== sort_index ==========')

# # 可以將已經列出的pd照著某些規則排列,ascending=True or False
# print(sales.sort_values(by = 'cup_cost',ascending=False))

# # sort_index可以排列左側(index的這欄)
# # axis 0 會依index排列也就是Billy Charly John Tim
# print(sales.sort_index(axis=0,ascending=True))

# # axis 1 會依欄位排列也就是上面會變成cup_cost red_wine white_wine的順序
# print(sales.sort_index(axis=1,ascending=True))