def solution(n):
    n=str(n)
    result=n[::-1]
    c=[]
    for i in range(0, len(result)):
        c.append(int((result[i]))) 
    return c