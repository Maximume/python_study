# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# 1. make list of prime numbers
# 2. find 10,001st number

# 3. prime number calculator!? I can recycle this code

prime_list = []
prime_factor = 0
limit = 500000
for i in range(2, limit):
    limit_i = int(i ** 0.5) + 1
    for j in range(2, limit_i):
        if i % j == 0:
            prime_factor += 1
    if prime_factor == 0:
       prime_list.append(i)
    prime_factor = 0
    if len(prime_list) == 10001:
        print(prime_list[10000])
        break

# 4. adjusting limit, calculate prime numbers over 10001, then find 10001st number
# +. also can be solved by keeping calculation, only when print value when 10001st number found