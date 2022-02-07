# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + 3 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# 1. find sum of the squares
# 2. find square of sum
# 3. find difference

sumOFsquares = 0
squareOFsum = 0
sum = 0
for i in range(100):
    sumOFsquares += i ** 2
    sum += i
squareOFsum = sum ** 2

difference = squareOFsum - sumOFsquares
print(difference)

# It can solve "LITERALLY"