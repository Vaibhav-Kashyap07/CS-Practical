num = int(input("Enter a number: "))
facts =[]

for i in range(1, num+1):
    if not num % i:
        facts.append(i)

if facts == [1, num]:
    print("It is a prime number.")
else:
    print("It is a composite number.")