# It is possible to show that the square root of two can be expressed as an infinite continued fraction.

# 2^(1/2) = 1 + 1/(2 + a), a = 1/(2 + a)

# By expanding this for the first four iterations, we get:

# 1 + 1/2 = 3/2 = 1.5
# 1 + 1/(2 + 1/2) = 7/5 = 1.4
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
# The next five expansions will be 41/29, 99/70, 239/169, 577/408, 1393/985 and so on...
 
# And 1393/985 is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

### The expression has been modified somewhat due to the limiation of fractional expression


# 1. thus every terms plused 1, remove 1 from every terms then we will get
# 1/2, 2/5, 5/12, 12/29, 29/70 ...

# 2. the denominator of previous term will be numerator and so on, and add 1 means add value of denominator to numerator

numerator = 3
denominator = 2
results = 0

for x in range(1+1, 1000+1):
    numerator, denominator = numerator + denominator * 2, numerator + denominator
    if len(str(numerator)) > len(str(denominator)): 
        results += 1
print (results)