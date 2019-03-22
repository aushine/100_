if __name__ == "__main__":
    a = int(input("input one num:"))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print(f"{a}{b}")