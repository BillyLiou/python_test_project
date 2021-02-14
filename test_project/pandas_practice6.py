#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   pandas_practice6.py
@Time    :   2021/02/14 23:54:44
@Author  :   Billy Liu
@Version :   1.0
@Contact :   billy@test.mail
@Desc    :   None
'''

import pandas as pd
import numpy as np

car_name = ['BMW','TOYOTA','MERCEDEZ']

res_list = []
for i in range(10):
    temp_list = [
        car_name[np.random.randint(low=0,high=3)],
        np.random.randint(low=1,high=1001)
    ]
    res_list.append(temp_list)

# 以下方法為將一個品牌作為group把後面的amount加總
df = pd.DataFrame(res_list,columns=['name','amount'])
df_sum = df.groupby(['name']).sum()
print(df_sum)
print('====================')

df_count = df.groupby(['name'],as_index=False)['name'].agg({'Count':'count'})
print(df_count)
