import time
start = time.clock()
for i in range(1000):
    print(i)
end = time.clock()
print(end - start)