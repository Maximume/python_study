# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

# 1. make factorial function

def facto(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

# 2. result to str to use index

str_fact100 = str(facto(100))

# 3. sum every index (digit)

sum = 0
for i in str_fact100:
    sum += int(i)
print(sum)