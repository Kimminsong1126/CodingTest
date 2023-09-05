a,b = input().split() #replace 함수는 str 형태로 입력받아야한다.

#즉 문자열을 바꾼 뒤 int로 변환해주는 느낌
min=int(a.replace('6','5'))+int(b.replace('6','5')) 
max=int(a.replace('5','6'))+int(b.replace('5','6'))

print(min, max)