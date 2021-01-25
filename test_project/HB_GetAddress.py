#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   HB_GetAddress.py
@Time    :   2021/01/14 10:54:40
@Author  :   Billy Liu
@Version :   1.0
@Contact :   billy@test.mail
@Desc    :   None
'''

import base64
from datetime import datetime
import time 
import json

t = time.time()
timestamp = int(datetime.fromtimestamp(t).timestamp())
appRequestTime = datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
appMethod = 'orderquery'
data_dict = {
    'timestamp': timestamp,
    'province': '110'
}
json_str = json.dumps(data_dict)
new_dict = json.loads(json_str)


with open("./JSON/address_data.json", "w",encoding='utf-8') as f:
    json.dump(new_dict, f,ensure_ascii=False)
    print('載入檔案完成')

# print(timestamp)
print(appRequestTime)


