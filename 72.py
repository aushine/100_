student = []
for i in range(5):
    student.append(['', '', []])
def input_(stu):
    for i in range(3):
        stu[i][0] = input("输入学号:")
        stu[i][1] = input("输入名字:")
        for j in range(3):
            stu[i][2].append(input("输入分数"))
    return stu
def output_(stu):
    num = input("输入学号")
    name = input("输入姓名")
    for i in stu:
        if i[0] == num and i[1]==name:
            print(f"学生分数为:{','.join(i[2])}")


output_(input_(student))
