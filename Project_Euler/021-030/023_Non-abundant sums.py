# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# 1. for checking deficient or abundant, function that calculate sum of divisors is needed

def sum_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

# 2. I need combination of two abundants, so make a list of abundant first

abundant = []
for i in range(1, 28123 + 1):
    sumofdiv = sum_divisors(i)
    if i < sumofdiv:
        abundant.append(i)

# 3. by mathematical analysis, for checking every positive integer, only check under 28123

target_numbers = set(range(28123+1))

comb_abun = []
for i, x in enumerate(abundant):
    for j, y in enumerate(abundant):
        sum = 0
        sum = abundant[i] + abundant[j]
        comb_abun.append(sum)
comb_abun = set(comb_abun)

# 4. sum of relative complement is the answer

checked = list(target_numbers - comb_abun)


sum = 0
for i in checked:
    sum += i
print(sum)