s = input("plz input one string:")
cn_string = 0
num = 0
en_string = 0
other_string = 0
space = 0
for each in s:
    if '\u4e00' <= each <= '\u9fff':
        cn_string += 1
    elif each.isalpha():
        en_string += 1
    elif each.isalnum():
        num += 1
    elif each == ' ':
        space += 1
    else:
        other_string += 1
print(f'中文字符共有:{cn_string} 英文字符共有:{en_string} 数字字符共有:{num} 其他字符共有:{other_string} 空格共有{space}个')
