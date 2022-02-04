# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# 1. should know prime numbers first
# 2. prime list limit should be smaller than root of 600851475143
# 3. find ou root of 600851475143
# 4. find out prime list
# 5. try to divide 600851475143 by arguments in prime list
# 6. the largest one is the largest prime factor of the number 600851475143


# limit = int(600851475143 ** 0.5) + 1 #less than 775146
# prime_list = []
# prime_factor = 0
# for i in range(2, limit):
#     limit_i = int(i ** 0.5) + 1
#     for j in range(2, limit_i):
#         if i % j == 0:
#             prime_factor += 1
#     if prime_factor == 0:
#        prime_list.append(i)
#     prime_factor = 0
# prime_factors = []
# for k in prime_list:
#     if 600851475143 % k == 0:
#         prime_factors.append(k)
# print(prime_factors) #[71, 839, 1471, 6857]

# the largest prime factor of the number 600851475143 = 6857
# but this solution takes a lot of time (over 30secs)
# how about find factors of 600851475143 limit by 1000 and figure out factors are prime then divide 600851475143 by prime factor first?

qValue = 600851475143

# factors_upto1000 = []
# for i in range(2, 1000):
#     if qValue % i == 0:
#         factors_upto1000.append(i)
# print(factors_upto1000) #[71, 839]

#check 71, 839 isPrime

def isPrimeNumber(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

# print(isPrimeNumber(71))    #True
# print(isPrimeNumber(839))   #True

qValue_divided = ((qValue / 71) / 839) / 1471   #1471 is Prime factor
print(qValue_divided)   #final qValue_divided is 6857
print(isPrimeNumber(6857))  # True

limit = int(qValue_divided ** 0.5) + 1
prime_list = []
prime_factor = 0
for i in range(2, limit):
    limit_i = int(i ** 0.5) + 1
    for j in range(2, limit_i):
        if i % j == 0:
            prime_factor += 1
    if prime_factor == 0:
       prime_list.append(i)
    prime_factor = 0
prime_factors = []
for k in prime_list:
    if qValue_divided % k == 0:
        prime_factors.append(k)
print(prime_factors)