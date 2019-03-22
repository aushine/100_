if __name__ == "__main__":
    a =[]
    for each in range(10):
        a.append([])
        for each_ in range(1, each+2):
            a[each].append(1)
    for i in range(2, 10):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1]+a[i-1][j]
    b = []
    for each in a:
        b.append(' '.join(map(str, each)))
    for each in b:
        print(each.center(26))
