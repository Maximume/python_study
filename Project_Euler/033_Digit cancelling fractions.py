# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

# 1. if a, b, c were single digit, form of combinations of these number will be ab/ac = b/c or ab/ca = b/c

# 2. turn into this form to fomular, (a*10 + b) / (a*10 + c) = b / c and so on.

# 3. case 1.

res = []
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(1, 10):
            if (a*10 + b)*c == (a*10 + c)*b and a*10+b != a*10+c:
                res.append([a*10+b, a*10+c, b, c])

# 4. case 1 seems to print out only trivial examples.

# 5. case 2.

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(1, 10):
            if (a*10 + b)*c == (c*10 + a)*b and a*10+b != c*10+a:
                res.append([a*10+b, c*10+a, b, c])

print(res)  #[[64, 16, 4, 1], [65, 26, 5, 2], [95, 19, 5, 1], [98, 49, 8, 4]]

# 6. four fractions came out! and given its lowest common terms (1/4, 2/5, 1/5, 1/8(=4/8))

# 7. product will be 1/100. so, denominator is 100