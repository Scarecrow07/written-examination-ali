#_*_ coding:utf-8 _*_

import pandas as pd
#import numpy as np
#import operator
#import collections
import itertools

#load data from file
list_base = []
with open('D:/Pycharm/exam_ali/data.txt') as f:
    for line in f.readlines():
        if line != '\n':
            list_base.append(line.strip())
print(list_base)

#parse the discount condition and money
meet_condition = []
discount = []
discount_condition = list_base[0].split(';')
for i in discount_condition:
    meet_condition.append(int(i[0:i.index('-')]))
    discount.append(int(i[i.index('-')-len(i)+1:]))

#parse goods price and discount type
price = []
discount_type = []
buycount = list_base[1].split(';')
for i in buycount:
    price.append(int(i[0:i.index('-')]))
    discount_type.append(int(i[i.index('-')-len(i)+1:]))

#parse the total money
total_fee = int(list_base[2])

price_length = len(price)
discount_type_count = max(discount_type)

#merge the price,discount type,discount condition,discount into 1 dataframe
meet_condition_merge = []
discount_merge = []
for i in range(len(discount_type)):
    meet_condition_merge.append(meet_condition[discount_type[i] -1])

for i in range(len(discount_type)):
    discount_merge.append(discount[discount_type[i] - 1])

data =pd.DataFrame({'price':price,
                    'discount_type':discount_type,
                    'meet_condition':meet_condition_merge,
                    'discount':discount_merge})

#create full permutation and calculate the total price
money_before_discount = []
money_after_dsicount = []
for i in itertools.product([0,1],repeat = price_length):
    data['price_new'] = data.price * i
    data_new = list(data.groupby(discount_type).sum().price_new)
    data_new1= list(data.groupby(discount_type).sum().price_new)
#goods money minus discount
    for j in range(discount_type_count):
        if data_new[j] >=meet_condition[j]:
            data_new[j] = data_new[j] - discount[j]
#pick the available money
        if sum(data_new)<=total_fee:
            money_after_dsicount.append(sum(data_new))
            money_before_discount.append(sum(data_new1))
#pick the max money before discount
output = max(money_before_discount)
print('最大的折扣钱价格为：',output)