x = int(input("Enter a number: "))
n = int(input("Enter the exponent: "))

sum = 0

for i in range(n+1):
    if i % 2: sum-=x**i
    else: sum+=x**i

print(f"Answer: {sum}")