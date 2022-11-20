x = int(input("Enter a number: "))
n = int(input("Enter the exponent: "))

sum = 0

for i in range(1, n+1):
    if i % 2: sum+=(x**i)/i
    else: sum-=(x**i)/i

print(f"Answer: {sum}")