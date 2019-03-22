#输入n 为偶数是调用函数求1/2+1/4
from functools import reduce
n = int(input("输入n值"))
list1 = []
if n % 2 == 0:
    list1 = [x for x in range(1, n+1) if x % 2 == 0]
else:
    list1 = [x for x in range(1, n+1) if x % 2 != 0]
list1 = list(map(lambda x: 1/x, list1))
print(reduce(lambda x, y: x+y, list1))