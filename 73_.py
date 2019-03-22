if __name__ == "__main__":
    ptr = []
    for i in range(5):
        ptr.append(int(input("输入一个整形数字:")))
    print(ptr[::-1])