#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""

import re


pattern = r"abc"
res = re.match(pattern, 'abcabc',flags=0);
if res:
    print(res.group())
    print(res.group())

