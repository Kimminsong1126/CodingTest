import math

def solution(numer1, denom1, numer2, denom2):
    denom=denom1*numer2+denom2*numer1
    numer=denom1*denom2
    gcd=math.gcd(denom,numer)
    return [denom//gcd, numer//gcd]