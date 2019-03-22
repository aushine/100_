if __name__ == "__main__":
    a = [1, 2, 3]
    b = [3, 4, 5]
    a.sort()
    print(a + b)
    a.extend(b)
    print(a)