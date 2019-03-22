def monkey(n):
    if n == 1:
        return 1
    return (monkey(n-1)+1)*2
print(monkey(10))