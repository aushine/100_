'''
两个乒乓球队进行比赛,各处三人,甲队a,b,c 乙队x.y,z 抽签决定比赛名单,
a 不可以和 x 比
c 不和 x,z比
'''
list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z']
name_list = []
for j in range(0, 3):
    for k in range(0, 3):
        name_list.append([list1[j], list2[k]])
for each in name_list:
    if each[0] == 'a' and each[1] == 'x':
        name_list.remove(each)
    elif each[0] == 'c' and each[1] == 'x' or each[0] == 'c' and each[1] == 'z':
        name_list.remove(each)
for each_ in name_list:
    print(each_[0], 'VS', each_[1])