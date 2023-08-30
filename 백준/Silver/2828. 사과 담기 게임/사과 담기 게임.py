n, m = map(int, input().split())
j = int(input())

left = 1
right = m
count = 0

for _ in range(j):
    apple = int(input())

    if left <= apple <= right:
        continue
    elif apple < left:
        count = left - apple + count
        left = apple
        right = left+m-1
    else:
        count = apple - right + count
        right = apple
        left = right-m+1

print(count)