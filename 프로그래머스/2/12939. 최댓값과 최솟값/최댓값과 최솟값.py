def solution(s):
    non_space=s.split(' ')
    array=[]
    for i in non_space:
        array.append(int(i))
    array.sort()
    small=array[0]
    big=array[len(array)-1]
    
    #for i in range(0, len(array)):
        #small=array[0]
        #big=array[i]
    
    return str(small) + ' ' + str(big)