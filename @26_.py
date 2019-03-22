def jpig(n):
    if n == 1:
        sum = 1
    else:
        sum = n * jpig(n-1)
    return sum
print(jpig(20))