for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{j}*{i}=', i*j, end=' ', sep='')
    print()
print('*'*65)
for i in range(9, 0, -1):
    for j in range(1, i+1):
        print(f'{j}*{j}=', i*j, end=' ', sep="")
    print()