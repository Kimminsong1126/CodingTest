def solution(money):
    answer = []
    cup=money//5500
    left=money%5500
    answer.append(cup)
    answer.append(left)
    return answer