#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   nba_test.py
@Time    :   2021/02/06 00:25:00
@Author  :   Billy Liu
@Version :   1.0
@Contact :   billy@test.mail
@Desc    :   None
'''

# 這邊是在測試把algorithms 引入進來的時候 if __name__ == '__main__':內的東西是否會跳過
# import algorithms

# print('這邊測試下～')
# algorithms.call_foo()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from nba_api.stats.static import players

df = pd.DataFrame(np.random.randint(low=1,high=11,size=25).reshape([5,5]), index=['A','B','C','D','E'],columns=['c1','c2','c3','c4','c5'])
print(df)

print(df.reindex(['A','B']))

# plt.plot(df['c2'],df['c5'],color='b')
# plt.show()


# player_dict = players.get_players()
# LeBron = [player for player in player_dict if player['full_name'] == 'LeBron James'][0]
# print(LeBron)

# Lebron_id = LeBron['id']