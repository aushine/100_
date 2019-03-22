from functools import reduce
#后一个分子是前一个的分子分母之和,后一个的分母就是前一个的分子
'''
a = 1
b = 2
list1 = []
list1.append(b/a)
flag = 0
while flag <= 18:
    b, a = a+b, b
    list1.append(b / a)
    flag += 1
print(reduce(lambda x, y: x+y, list1))
'''
a = 2
b = 1
res =[]
res.append(a/b)
for i in range(19):
    a, b = a+b, a
    res.append(a/b)
print(reduce(lambda x, y: x+y, res))