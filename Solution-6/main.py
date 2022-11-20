num = int(input("Enter a number: "))

perfect = armstrong = palindrome = False
x = 0

for i in range(1, num):
    if not num % i:
        x += i
perfect = num == x
x= 0

digits = [int(_) for _ in str(num)]
exp = len(digits)
for digit in digits:
    x+=digit**exp
armstrong = num == x

palindrome = digits == digits[::-1]

print(f"Perfect: {perfect}")
print(f"Armstrong: {armstrong}")
print(f"Palindrome: {palindrome}")