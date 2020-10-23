#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import pandas as pd

gender = ["Male", "Male", "Female", "Male",
          "Male", "Male", "Female", "Male", "Male"]
name = ["蒙其·D·魯夫", "羅羅亞·索隆", "娜美", "騙人布",
        "文斯莫克·香吉士", "多尼多尼·喬巴", "妮可·羅賓", "佛朗基", "布魯克"]

analysis_data = pd.DataFrame(gender, columns=['gender'],index=name)
print(analysis_data)
print(pd.value_counts(analysis_data.gender))

# pandas .value_counts()
print('========== Categorical Variable ==========')
print(analysis_data['gender'].value_counts(normalize=True))
# analysis_data.value_counts(normalize=True) 此dictionary只有一個欄位['gender'],
# 因此跟直接查這個DataFrame的value_count是一樣的
print()