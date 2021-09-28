import pandas as pd
from CFDminer_test import Gcgrowth
'''
1、加载csv文件，将第一行作为属性集，得到一个list
2、将每一列加载到一个list当中，再将每个list加入到Sub_attrs这个list当中，方便做下一步处理
'''
if __name__ == '__main__':
    Dom_attrs = [] #将表头的一行作为属性值的集合存入其中
    Sub_attr = [] #存储每一列中的属性的具体的值
    Sub_attrs = [] #将所有具体的值存储成一个列表
    k = 3
    attrs = pd.read_csv('1.csv')
    df = pd.DataFrame(attrs)
    Dom_attrs = df.columns.tolist()
    for i in range(len(Dom_attrs)):
        Sub_attr.append(df[Dom_attrs[i]].tolist())
    for i in range(len(Sub_attr)):
        Sub_attrs.append(Sub_attr[i])
    g = Gcgrowth()
    k = g.gcgrowth(Dom_attrs,Sub_attrs,df,k)



