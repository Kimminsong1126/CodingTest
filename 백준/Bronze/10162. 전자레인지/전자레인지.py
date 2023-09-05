t = int(input())
a=0
b=0
c=0

if t % 10 != 0:
    print(-1)
else:
    while (t != 0):
        if t >= 300:
            a = t // 300
            t = t % 300
        elif t < 300 and t >= 60:
            b = t // 60
            t = t % 60
        elif t<60 and t>=10:
            c = t // 10
            t = t % 10
    print(a, b, c)
