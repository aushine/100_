from sys import stdout
n = num = int(input('input one interger:'))#保留初始值
f = []
for i in range(int(n/2+1)):
    for j in range(2, n+1):
        if n % j == 0:
            f.append(j)
            n //= j
            break
print("*".join(map(str, f)), "=", num, sep='')