x = int(input("Enter a number: "))
n = int(input("Enter the exponent: "))

sum = x

for i in range(2, n+1):
    fact = 1
    for _ in range(1,i+1):
        fact = fact * _

    if i % 2: sum-=(x**i)/fact
    else: sum+=(x**i)/fact

print(f"Answer: {sum}")