for each in range(100, 999):
    x = int(str(each)[0])
    y = int(str(each)[1])
    z = int(str(each)[2])
    if x**3 + y**3 +z**3 == each:
        print(each)