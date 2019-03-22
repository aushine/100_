while True:
    num = int(input('请输入一个数字:'))
    n = num
    if num**2 > 50:
        print(f'{num}的平方是{num**2}')
    else:
        print(f'{num}的平方是{num**2}')
        print(f'键入数字的平方数小于50,系统即将推出')
        break