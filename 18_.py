from sys import stdout
from functools import reduce
'''
for j in range(2, 1001):
    k = []
    n = -1
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i#减去每一个因子
            k.append(i)
    if s == 0:#s减到0说明该数可以被自己的因子整除,满足题目条件
        print(j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n])
'''
for i in range(2, 1001):
    res = []
    for j in range(1, i):
        if i % j == 0:
            res.append(j)
    if reduce(lambda x, y: x+y, res) == i:
        print(i, '=', end='', sep='')
        print(' * '.join(map(str, res)))
#将一个数所有的因子收集进res列表中,再把列表中所有元素相加.
#如果等于那个数
#就说明是一个"完数"