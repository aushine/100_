a, b, c = map(int, input("请输入三个整数,用空格隔开").split(' ', 2))
num = [a, b, c]
for i in range(2):
    for j in range(2-i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print(num)
