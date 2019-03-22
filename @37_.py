if __name__ == '__main__':
    list1 = []
    flag = 1
    while True:
        list1.append(int(input(f"请任意输入第{flag}个数字:")))
        flag += 1
        if len(list1) == 10:
           break
    for i in range(len(list1)-1):
        for each in range(len(list1)-1-i):
            if list1[each] > list1[each+1]:
                list1[each], list1[each+1] = list1[each+1], list1[each]
    print(list1)