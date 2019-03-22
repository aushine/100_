if __name__ == "__main__":
    s = 1
    sum = 0
    for i in range(1, 9):
        if i == 1:
            s = 4
        elif i == 2:
            s = 4 * 7
        if i > 2:
            s *= 8
        sum += s
        print(f"{s}")