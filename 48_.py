if __name__ == '__main__':
    a, b = map(int,input('请键入两个数字,空格分隔:').split(' ', 1))
    if a > b:
        print(f'{a}大于{b}')
    elif a < b:
        print(f'{a}小于{b}')
    elif a == b:
        print(f'{a}等于{b}')
    else:
        print('unknow')