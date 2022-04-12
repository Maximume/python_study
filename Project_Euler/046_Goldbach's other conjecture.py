# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import time
start = time.time()

def call_prime_list(n:int) -> list:
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

i = 3
checker = 0
primes = call_prime_list(10000)
while True:
    print("checking ", i)
    for p in primes:
        if checker == 1:
            break
        if p <= i:
            num = ((i - p) / 2) ** 0.5
            if num == int(num):
                checker += 1

    if checker == 0:
        print(i)
        break

    checker = 0
    i+=2

end = time.time()
print(end - start)