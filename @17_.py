from functools import reduce
from sys import stdout
n1 = input("请输入一个数:")
n2 = input("累加执行次数")
res = []
for each in range(1, int(n2)+1):
    res.append(n1 * each)
print((reduce(lambda x, y: x+y, map(int, res))))
