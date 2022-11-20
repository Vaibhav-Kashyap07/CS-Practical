string = input("Enter a string: ")
count = {"Vowels": 0, "Consonants":0, "Uppercase":0, "Lowercase":0}
for c in string:
    if c.isalpha():
        if c in "aeiou":
            count["Vowels"] += 1
        else: 
            count["Consonants"] += 1
        if c.islower():
            count["Lowercase"]+=1
        else:
            count["Uppercase"]+=1

for x in count:
    print(f"{x}: {count[x]}")