

#while 循环遍历列表中的元素

nums = [11,22,33,44,55]

nums_length = len(nums)         #需要确认列表中的元素的个数，根据下标取列表中的元素
i = 0
while i < nums_length:
    print(nums[i])
    i += 1

#for循环遍历列表中的元素，不用控制元素的个数以及下标
for num in nums:
    print(num)