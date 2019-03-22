if __name__ == "__main__":
    a = [6, 5, 4, 3, 2, 1]
    for each in range(len(a)//2):
        a[each], a[-each-1] = a[-each-1], a[each]
    print(a)