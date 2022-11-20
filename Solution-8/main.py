rec = int(input("Enter the number of recursion: "))
cur = [0, 1]
fib=[0]
for i in range(rec-1):
    fib.append(cur[0] + cur[1])
    cur[0] = cur[1]
    cur[1] = fib[-1]

print("\n".join([str(n) for n in fib]))