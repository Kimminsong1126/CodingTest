def solution(arr):
    sum=0
    for i in arr:
        sum+=i
    middle=sum/len(arr)
    return middle