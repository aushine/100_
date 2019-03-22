s_ = input("请输入年月日,空格隔开:")
year_, month_, day_ =s_.split(' ', 2)
year_ = int(year_)
month_ = int(month_)
day_ = int(day_)
month ={1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12:31}
print(type(month))
s = 0
for each in range(1, int(month_)):
    s += month[each]
if year_ % 4 == 0 and year_ % 100 != 0:
    print(s+int(day_)+1)
else:
    print(s+int(day_))

