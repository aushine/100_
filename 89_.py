data = list(input("input data:"))
data[1], data[2] = data[2], data[1]
data[0], data[3] = data[3], data[0]
for each in range(len(data)):
    data[each] = (int(data[each])+5) % 10
print(data)
