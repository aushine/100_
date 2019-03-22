if __name__ == '__main__':
    flag = 1
    list1 = []
    while True:
        in_ = input(f"输入第{flag}组三个数,每个数使用空格分隔:").split(" ", 2)
        in_ = list(map(int, in_))
        list1.append(in_)
        if flag == 3:
            break
        flag += 1
    res = 0
    print(list1[0][0], list1[1][1], list1[2][2])
    for each in range(3):
        print('X-man')
        res += list1[each][each]
    print(res)