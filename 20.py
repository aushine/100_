from functools import reduce
def bounce(n):
    list1 = [50, 150]
    if n == 1:
        return list1[0]
    return bounce(n-1)/2
print('第十次反弹高度:', bounce(10))
res = 150.0
list1 = [res]
for i in range(10):
    res /= 2
    list1.append(res)
print("总经过高度:", reduce(lambda x, y: x + y, list1))