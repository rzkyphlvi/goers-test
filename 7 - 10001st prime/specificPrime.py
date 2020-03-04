import math

targetIndex = 10001
primes = [2,3]

def calcPotentialPrimes(n):
    return [6*n-1, 6*n+1]

def isPrime(x):
    for p in primes:
        if p <= math.sqrt(x):
            if x % p == 0:
                return False
        else:
            break
    return True

i = 1
while True:
    potentialPrimes = calcPotentialPrimes(i)
    newPrimes = [x for x in potentialPrimes if isPrime(x)]
    primes += newPrimes

    if len(primes) >= targetIndex:
        break

    i += 1

print(primes[targetIndex-1])