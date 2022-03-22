# Euler discovered the remarkable quadratic formula:

# n^2 + n + 41

# It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39. However, when n = 40, 40^2 + 20 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

# The incredible formula n^2 -19 + 1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| <= 1000

# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

import time

start = time.time()

def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

def is_prime(n):
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

primes1000 = sieve(1000)

primes = primes1000[:]

largest = 0

for b in primes1000:
	for a in primes1000:
		i = 0
		while True:
			quadratic = i**2+a*i+b
			if quadratic not in primes:
				if is_prime(quadratic):
					primes.append(quadratic)
				else:
					if i-1 > largest:
						largest = i-1
						axb = a*b
					break
			i += 1
		i = 0
		while True:
			quadratic = i**2-a*i+b
			if quadratic not in primes:
				if is_prime(quadratic) and quadratic>0:
					primes.append(quadratic)
				else:
					if i-1 > largest:
						largest = i-1
						axb = -1*a*b
					break
			i += 1

print(axb)

print(time.time() - start) 