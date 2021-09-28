import os
import numpy as np
import xlwt
import pandas as pd
class HashTable(object):
    """
    哈希表类
    """
    def __init__(self):
        """
        初始化
        """
        self.__key_llist = []
        self.__val_list = []

    def add(self, key, val):
        """
        添加元素
        """
        self.__key_llist.append(key)
        self.__val_list.append(val)

    def get(self, key):
        """
        搜索元素
        """
        return self.__val_list[self.__key_llist.index(key)] if key in self.__key_llist else None

    def travel(self):
        """
        遍历哈希表
        """
        for index in range(0, len(self.__key_llist)):
            print(self.__val_list[index])
class Gcgrowth(object):
    def __init__(self):
        self.dater = []
        self.sater = []

    def gcgrowth(self, dater: list, sater: list,df = pd.DataFrame) -> list:
        '''

        :param dater:属性集
        :param sater: 属性
        :return: 返回一个由整型组成的二维数组
        dater和sater都是由属性构成的集合，但是由于gcgrowth仅仅支持整型变量，所以这个地方
        先建立一个每个属性和对应整型之间的映射
        先遍历整个列表，由出现的先后顺序构建映射
        '''
        Domattrs = dater
        Subattrs = sater
        temp = []
        '''
        将Subattrs中的元素进行过滤，将重复出现的属性给清除，然后返回到temp列表当中
        '''
        for i in range(len(Subattrs)):
            for j in range(len(Subattrs[i])):
                if Subattrs[i][j] not in temp:
                    temp.append(Subattrs[i][j])
        '''
        对subattrs进行第二次遍历，然后在temp中寻找对应的元素以便进行下一步处理
        '''
        ht = HashTable()
        new_list = []
        wb = xlwt.Workbook()
        wh = wb.add_sheet('1')
        k = 0
        for i in range(len(temp)):
            ht.add(temp[i], i+8)
        for i in range(len(Subattrs)):
            for j in range(len(Subattrs[i])):
                new_list.append(ht.get(Subattrs[i][j]))
        for i in range(len(Domattrs)):
            for j in range(len(df)):
                wh.write(j,i,new_list[k])
                k = k + 1
        matrix = df.values
        for i in  range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = ht.get(matrix[i][j])
        df2 = pd.DataFrame(matrix)
        df2.to_csv('t1.csv',index=False,header=False)
        t = os.system("GcGrowth t1.csv 3 rabbit")

        return temp

