#方法一:
a=[2,3,4,5]
b=[2,5,8]
tmp = [val for val in a if val in b]
print(tmp)
#[2, 5]

#方法二 比方法一快很多！
print(list(set(a).intersection(set(b))))
