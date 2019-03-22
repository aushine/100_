profit = int(input("请输入本月总利润(单位:万元):"))
arr = [1000000, 600000, 400000, 200000, 100000, 0]
rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
list1 = dict(zip(arr, rat))
r = 0
for k, v in list1.items():
    if profit > k:
        r += (profit-k) * v
        profit = k

print(f"本月总奖金为:{r}")
