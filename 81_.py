for x in range(10, 100):
    if 809 * x == 800 * x + 9 * x:
        if len(str(809 * x)) == 4:
            if len(str(9 * x)) == 3:
                print(f"809*{x}={809*x}")
                break