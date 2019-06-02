from math import sqrt, floor

def isFactor(dividend, divisor):
    if dividend % divisor == 0:
        return True
    return False

def isPrime(n):
    for i in range(2, floor(sqrt(n)) + 1):
        if isFactor(n, i):
            return False
    return True

def genPrimes(k):
    primeCounter = 0
    seqCounter = 2
    while primeCounter < k:    
        if isPrime(seqCounter):
            print(seqCounter, end= ' ')
            primeCounter += 1
        seqCounter += 1