nums=[1,-10,3,4,-4]
n=len(nums)
start=0
min_value_in_nums=nums[start]
for i in range(1,n):
    if nums[i]<nums[start]:
        min_value_in_nums=nums[i]
        start+=1

print(min_value_in_nums)