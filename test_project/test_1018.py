#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 12:20:55 2020

@author: billyliou
"""


def sum(num1: int, num2: int) -> int:
    """
    :type num1: int
    :type num2: int
    :rtype: int
    """
    res = num1 + num2
    print(str(res))
    return res

sum(5,6)