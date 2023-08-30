n = int(input())
c=[]
result=0

for _ in range(n):
    c.append(int(input()))

c.sort(reverse=True)

for i in range(n):
    if (i+1)%3==0:
        continue
    result+=c[i]

print(result)
