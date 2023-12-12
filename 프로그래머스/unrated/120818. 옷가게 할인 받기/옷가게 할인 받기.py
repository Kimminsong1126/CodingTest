def solution(price):
    if price>=500000:
        price*=0.8
    elif 300000<=price:
        price*=0.9  
    elif price>=100000:    
        price*=0.95
    return int(price)