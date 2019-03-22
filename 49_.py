MAXIMUM = lambda x, y: (x > y) and x or (x < y) and y
MINIMUM = lambda x, y: (x > y) and y or (x < y) and x
if __name__ == '__main__':
    a = 10
    b = 20
    print ('The largar one is %d' % MAXIMUM(a, b))
    print ('The lower one is %d' % MINIMUM(a, b))