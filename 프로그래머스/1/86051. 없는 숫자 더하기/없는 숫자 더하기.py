def solution(numbers):
    a=[1,2,3,4,5,6,7,8,9]
    count=0
    for k in numbers:
        for i in range(1,10):
            if k==i:
                a.remove(k)
                
    return sum(a)