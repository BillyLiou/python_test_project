#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   PandasPractice5.py
@Time    :   2021/02/06 01:27:17
@Author  :   Billy Liu
@Version :   1.0
@Contact :   billy@test.mail
@Desc    :   None
'''


import pandas as pd 
import numpy as np


# 可以用doc string 來註解function
def testa():
    """
    this is a doc string for testa function()
    """
    print('testa function')

print(testa.__doc__)

df = pd.DataFrame(
    np.random.randint(low=1,high=11,size=36).reshape([6,6]),
    index=[i+1 for i in range(6)],
    columns=['c'+str(i+1) for i in range(6)])

print(df)