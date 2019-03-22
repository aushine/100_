#输入一个数组,最大的鱼第一个元素交换,最小的和最后一个元素交换
flag = 1
nums = []
while True:
    nums.append(int(input(f'请输入第{flag}个数:')))
    flag += 1
    if flag == 7:
        break
for each in range(len(nums)):
    if nums[each] == max(nums):
        nums[each], nums[0] = nums[0], nums[each]
    if nums[each] == min(nums):
        nums[each], nums[-1] = nums[-1], nums[each]
print(nums)