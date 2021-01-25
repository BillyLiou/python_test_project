#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   createjson.py
@Time    :   2021/01/07 15:19:33
@Author  :   Billy Liu
@Version :   1.0
@Contact :   billy@test.mail
@Desc    :   None
'''

import json


n = 5
sequence = 1002
test_dict = {
    "createTime": "20210107151259", 
    "creator": "60003833", 
    "creatorName": "张3", "mallCode": "000001", "orderId": "40001000037210107470001", "productList": [], 
    "remarks": "", "storeCode": "100102", "storeName": "演示产品库", "totalCount": 1, "type": "40", "status": "COMPLETED", "statusText": "已完成"
}


def createOrder(dict1,num,orderId: str):
    dict1["orderId"] = "4000100003721010747"+str(orderId)
    dict1["totalCount"] = num
    for i in range(num):
        tmpItem = str(i+1).zfill(4)
        tmp = {
            "index": i, "isBatchManage": "0", "isSerialCodeManage": "1", "itemCode": "740010"+tmpItem, "itemName": "米家冰箱", "itemCount": 1, "serialCode": "", "inStore": "100102", "inStoreName": "演示产品库", "outStore": "100102", "outStoreName": "演示产品库"
        }
        dict1['productList'].append(tmp)

createOrder(test_dict,n,sequence)


json_str = json.dumps(test_dict)
new_dict = json.loads(json_str)


with open("./JSON/example.json", "w",encoding='utf-8') as f:
    json.dump(new_dict, f,ensure_ascii=False)
    print('載入檔案完成')

