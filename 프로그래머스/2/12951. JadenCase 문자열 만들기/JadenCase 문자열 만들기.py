def solution(s):
    s=s.split(" ")
    result=[]
    for i in s:
        result.append(i.capitalize())
    
    return ' '.join(result)
