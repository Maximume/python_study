# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

# 1. make function find divisors

def sum_divisors(n):
    d_n = 0
    for i in range(1, n):
        if n % i == 0:
            d_n += i
    return d_n

# 2. under 10000 list
target = list(range(10000 + 1))

sum = 0
for num in target:
    d_n = sum_divisors(num)
    pair = sum_divisors(d_n)

    if num == pair and num != d_n:
        print(num, d_n)
        sum += num + d_n
        target.remove(d_n)

print(sum)