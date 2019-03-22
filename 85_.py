#输入一个奇数,判断最少几个9处于该数为整
nine = '9'
n = int(input("输入一个奇数:"))
while True:
    if int(nine)/n % 1 == 0:
        print(f"{nine}/{n}={int(int(nine)/n) }")
        break
    else:
        nine += "9"