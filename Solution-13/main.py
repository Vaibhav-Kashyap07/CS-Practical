nums = input("Enter list of numbers: ")
nums = [int(n) for n in nums.split(",")]

for i in range(len(nums)):
    if not i % 2 and i+1 < len(nums):
        n = nums[i]
        nums[i] = nums[i+1]
        nums[i+1] = n
print(nums)