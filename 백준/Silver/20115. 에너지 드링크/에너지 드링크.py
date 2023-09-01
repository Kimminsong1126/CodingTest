n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

result = a[0]
for i in range(1, n):
    result += a[i] / 2

print('%g'%result)