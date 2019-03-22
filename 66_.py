flag = 1
nums = []
while flag <= 3:
    nums.append(int(input(f"请输入第{flag}个数:")))
    flag += 1
for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j] > nums[j+1] :
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums)