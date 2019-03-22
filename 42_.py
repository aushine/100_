num = 2
def autofunc():
    num = 1
    print(f'internal block num = {num}')
    num += 1
for i in range(3):
    print(f'the num ={num}')
    num += 1
    autofunc()