# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# 1. Prime number again! I can recycle my prime number check program

prime_list = []
prime_factor = 0
limit = 2000000
for i in range(2, limit):
    limit_i = int(i ** 0.5) + 1
    for j in range(2, limit_i):
        if i % j == 0:
            prime_factor += 1
    if prime_factor == 0:
       prime_list.append(i)
    prime_factor = 0
sum = 0
for i in prime_list:
    sum += i
print(sum)