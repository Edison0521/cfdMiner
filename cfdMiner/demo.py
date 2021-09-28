from CFDminer_test import HashTable
import pandas as pd
pair = open('rabbit.pair','r')
close = open('rabbit.closed','r')
key = open('rabbit.key','r')
def getindex(lst=None, item=''):
    return [index for (index,value) in enumerate(lst) if value == item]
def Gcreadfiles(filename):
    labels = []
    for line in filename.readlines():
        labels.append(line.split())

    for i in range(len(labels)):
        for j in range(len(labels[i])):
            labels[i][j] = int(labels[i][j])
    return labels
'''
自由项集转换成列表之后的配对
key_list 是自由项集出现的具体属性
key_hash 是自由项集出现的次数
'''
g_key = Gcreadfiles(key)
key_list = g_key
hash_key = []
#del key_list[0]
for i in range(len(key_list)):
    #del key_list[i][0]
    hash_key.append(key_list[i][len(key_list[i]) - 1])
    del key_list[i][len(key_list[i])-1]

'''
closed 是封闭项集
closed_list 是封闭项集中具体的属性
hash_closed 是封闭项集中对应属性出现的次数
'''
g_close = Gcreadfiles(close)
closed_list = g_close
hash_close = []
#del closed_list[0]
for i in range(len(closed_list)):
    #del closed_list[i][0]
    hash_close.append(closed_list[i][len(closed_list[i]) - 1])
    del closed_list[i][len(closed_list[i])-1]

'''
pair 是自由项集和封闭项集之间的hash值，对应论文中具体出现的C2F
'''
g_pair = Gcreadfiles(pair)
pair_list = g_pair
hash_key_pair = [] #封闭项集
hash_val_pair = [] #自由项集
#del pair_list[0]
for i in range(len(pair_list)):
    hash_key_pair.append(pair_list[i][len(pair_list[i]) - 1])
    hash_val_pair.append(pair_list[i][0])
pair_ht = HashTable()
RHS = []
temp_list1 = []
for i in range(len(pair_list)):
    pair_ht.add(pair_list[i][0],pair_list[i][1])
RHS = []
for i in range(len(g_close)):
    RHS.append(getindex(hash_key_pair,i))
for i in range(len(RHS)):
    for j in range(len(RHS[i])):
        if i == RHS[i][j]:
            RHS[i][j] = None
for i in range(len(RHS)):
    res = list(filter(None, RHS[i]))
    temp_list1.append(res)
#RHS = list(filter(None,temp_list1))
#RHS = temp_list1
temp_list2 = []
L = RHS #L中存放每个开项集







