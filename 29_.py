intger = input('请输入已给不多于5位的正整数:')
if len(intger) >5:
    print("请输入5位数以内的数.")
else:
    print(f'这个数是{len(intger)}位数,逆序输出结果为:{" ".join(intger[::-1])}')