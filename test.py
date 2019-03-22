from functools import reduce
'''from functools import reduce
list1 = [1, 2, 3, 4]
list1 = reduce(lambda x, y: x+y, list1)
print(type(list1))
'''
'''
list1 = [1, 2, 3]
print("*".join(map(str, list1)))
'''
# list1 = [1, 2, 3]
# print(reduce(lambda x, y: x/y, list1))
'''
a = 2.0
b = 1.0
l = []
l.append(a / b)
for n in range(1, 20):
    b, a = a, a + b
    l.append(a / b)
print (reduce(lambda x, y: x + y, l))'''
''''
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)'''
'''
#dict1 = {1:"233"}
#print(dict1[1][2])
a, b = 1, 2
print(a,b)

s = sorted([9,8,7,6,5,4,3,2,1], reverse=True)
print(s)
'''
'''
res =[]
for each in range(2, 100):
    for j in range(2, each//2):
        print(each)
        if each % j == 0:
            if each == 4:
                print("fuck")
            break
    else:
        res.append(each)
list1 = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
list2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(len(list1), len(list2))
print(res)
'''
'''
res = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        res.append(i)
print(res)
'''
'''
res = []
for i in range(11):
    res.append('1'*(i+1))
    res[i] = [x for x in res[i]]
for i in range(2, 11):
    for j in range(1, i):
        res[i][j] = str(int(res[i-1][j-1])+int(res[i-1][j]))
for each in res:
    print(' '.join(each).center(25))
'''
'''
lisst1 = ["fucking", "crazy", 'English', "fuck"]
lisst1.sort(key=lambda x: x[2])
print(lisst1)
'''
'''
res = []
for i in range(10):
    res.append(list('1'*(i+1)))
for i in range(2, 10):
    for j in range(1, i):
        res[i][j] = str(int(res[i-1][j-1])+int(res[i-1][j]))
for each in range(len(res)):
    res.insert((each+1)+each, "\n")
'''
'''
res = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        res.append(i)
print(res)
'''
'''
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
        '''
'''
x = list(range(1, 35))
count = 1
while len(x) > 1:
    x_ = x[:]
    for i in range(len(x_)):
        count += 1
        if count % 3 == 0:
            x.remove(x_[i])

list_test = [[[[x, y], [z, h], [k, j]], [[l, m], [o, p]]]for x in range(1, 10) 
             for y in range(1, 10) for z in range(1, 10) 
             for h in range(1, 10)for j in range(1, 10)
             for k in range(1, 10) for l in range(1, 10)
             for m in range(1, 10) for n in range(1, 10) 
             for o in range(1, 10)for p in range(1, 10)
             for p in range(1, 10 for q in range(1,10))]
print(list_test)
'''
'''
for i in range(2, 100):
    for j in range(2, i):
        if i == 99:
            print("fuck")
        if i % j == 0:
            break
    else:
        print(i)
'''
'''
i = 0
j = 1
x = 0
while (i < 5):
    x = 4 * j
    for i in range(5):
        if x % 4 != 0:
            break
        else:
            i += 1
            x = (x/4) * 5 + 1
    j += 1
print(x, j)
'''
'''
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
        elif i == j+1:
            print(i)
'''
'''
x = 1.5
y = 1.0
print(y % 1==0 )
'''
'''
i = 0
j = 1
x = 0
while i != 5:
    x = 4 * j
    for i in range(5):
        if x % 4 != 0:
            break
        else:
            i += 1
            x = (x/4) * 5 + 1
    j += 1
print(x)
i = 0
j = 1
x = 0
while i != 5:
    x = j * 4
    for i in range(5):
        if x % 4 !=0:
            break
        else:
            i += 1
            x = (x / 4) * 5 + 1
    j += 1
print(x)
'''
