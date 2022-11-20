num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

prod = num1*num2
def getGCD(a, b):
    if(b == 0):
        return abs(a)
    else:
        return getGCD(b, a % b)

gcd = getGCD(num1, num2)

print(f"Greatest Common Divisor: {gcd}")
print(f"Least Common Multiple: {prod//gcd}")