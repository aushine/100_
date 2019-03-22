string = [5, 6, 7, 8, 9, 19]
for i in range(len(string)-1):
    for j in range(len(string)-1-i):
        if string[j] > string[j+1]:
            string[j], string[j+1] = string[j+1], string[j]
print(string)