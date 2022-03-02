# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def remainder(i, r):
    return 10 * r % i

gc = 0
gci = 0
re = []
for i in range(2, 1000):
    remainders = [1]
    while True:
        remainders.append(remainder(i, remainders[-1]))
        if remainders[-1] in remainders[0 : -1] or remainders[-1] == 0:
            if len(remainders) > gc:
                gc = len(remainders)
                gci = i
            break

print(gci)  #983
