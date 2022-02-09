# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# 1. There is only one Pythagorean triplet, so one list is enought

res_list = []

# 2. I already know sum of a, b, c
# 3. That means, if I fix a and b, c is automatically fixed
# 4. find all combinations of a, b, c then check these are Pythagorean triplet

for a in range(1, 1000):
    for b in range(a, 1000):
        c = 1000 -a -b
        if c**2 == a**2 + b**2:
            print('got it')
            res_list = [a, b, c]
print(res_list)
res = res_list[0] * res_list[1] * res_list[2]
print(res)