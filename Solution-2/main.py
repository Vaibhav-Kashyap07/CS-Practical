num1 = input("Enter number one: ")
num2 = input("Enter number two: ")

larger = smaller = num1

if num2 > larger:
    larger = num2
elif num2 < smaller:
    smaller = num2
else:
    print("Both Numbers are equal.")
    exit()

print(f"Larger: {larger}\nSmaller:{smaller}")