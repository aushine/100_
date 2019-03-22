if __name__ =="__main__":
    print('初始列表:', end='')
    a = [1, 4, 6, 9, 13, 17, 19, 28, 40, 100]
    insert = int(input('键入一个正整数插入:'))
    for each in range(len(a)):
        if a[each] < insert < a[each+1]:
            a.insert(a.index(a[each])+1, insert)
            break
print(a)