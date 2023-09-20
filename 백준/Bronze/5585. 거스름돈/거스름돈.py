n = int(input())

n = 1000 - n
result = 0

for i in [500, 100, 50, 10, 5, 1]:
    while i <= n:
        n -= i
        result += 1

print(result)