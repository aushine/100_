from functools import reduce
print('%e'%reduce(lambda x, y: x*y, [x for x in range(1, 101)]))

