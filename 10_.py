'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    c = 1
    while (n-2) >0:
        c = a+b
        a = b
        b = c
        n -= 1
    return c
print(fib(5))
'''
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(7))