n1 = 100#初始高度
res = 0
#每次触底后到反弹到原高度的一半
for i in range(10):
    res += n1/2
    n1 /= 2
print(res)