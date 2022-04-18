# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# It is not until n=23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of nCr for 1 <= n <= 100, are greater than one-million?

# 1. define factorial, nCr

import time

start = time.time()

def factorial(n):
    facto = 1
    for i in range(1, n + 1):
        facto *= i
    return facto

def nCr(n, r):
    return factorial(n) / factorial(r) / factorial(n-r)

cnt = 0

for n in range(1, 100 + 1):   # 2. 1<= n <= 100
    for r in range(1, n + 1):
        if nCr(n, r) > 1000000:
            cnt += 1

print(time.time() - start)
print(cnt)