#两个3行3列的矩阵,实现对应位置的数据相加,并返回一个新矩阵
X = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
Y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
for each in range(3):
    for each_ in range(3):
        X[each][each_] += Y[each][each_]
for each1 in X:
    print(each1)