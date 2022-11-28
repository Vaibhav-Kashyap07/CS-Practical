nums = input("Enter list of numbers: ")
nums = [int(n) for n in nums.split(",")]
print(f"Largest: {max(nums)}")
print(f"Largest: {min(nums)}")