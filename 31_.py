week = {'周一': 'M', '周二': 'TU', '周三': 'W', '周四': 'TH', '周五': 'F', '周六': 'SA', '周日': 'SU'}
l1 = week.keys()
l2 = week.values()
week = dict(zip(l2, l1))
s1 = input('请输入第一个字母:')
if s1 == 'M'or s1 == 'W' or s1 == 'F':
    print(week[s1])
else:
    s1 += input("仅一个字母不可判断,请输入第二个:")
    print(week[s1])
