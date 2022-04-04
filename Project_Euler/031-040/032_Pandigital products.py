# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# 1. fomula will be a x b = a * b

# 2. make these numbers as string, set(str(a) + str(b) + str(a*b)) == set('123456789')

# 3. at the same time, pandigital does not allow duplication, each digit must contained 1 time

# 4. by 3. len(a) + len(b) + len(a*b) == 9
#   if len(a) == 1, len(b) == 4, len(a*b) == 4
#                   len(b) == 3, len(a*b) == 5 <- impossible
#   if len(a) == 2, len(b) == 3, len(a*b) == 4
#                   len(b) == 2, len(a*b) == 5 <- impossible
#   if len(a) == 3, already checked case (by len(b) == 3)

# 5. only 2 cases possible

res = []

for a in range(1, 10):
    for b in range(1000, 10000):
        num_str = str(a) + str(b) + str(a*b)
        if len(num_str) != 9:
            continue
        if set(num_str) == set('123456789'):
            res.append(a*b)
        elif len(num_str) > 9:
            break

for a in range(10, 100):
    for b in range(100, 1000):
        num_str = str(a) + str(b) + str(a*b)
        if len(num_str) != 9:
            continue
        if set(num_str) == set('123456789'):
            res.append(a*b)
        elif len(num_str) > 9:
            break

tot = 0
for i in set(res):
    tot += i

print(tot)