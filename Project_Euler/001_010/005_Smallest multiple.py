# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# 1. It means find least common multiple
# 2. First, I have to find Prime Numbers 2 to n
# 3. and then, replace arguments of prime numbers with square number and multiple them all
# 4. 4 is 2^2 so replace 2, 16 is 4^4 so replace 4
# 5. how about 8? 2 should replace by 4, and 4 -> 8, and 8 -> 16
# 6. same solution should adapt to 3, 5, 7 ... 

# or using LCM, GCD

# 1. It means find least common multiple (LCM)
# 2. We alreay know LCM always comes with GCD
#   A = GCD * a, B = GCD * b
#   LCM = GCD * a * b
# 3. find GCD first, then find LCM
# 4. how to find GCD?
# 5. a%i=0 and b%i=0 <- CD, make it Greatest(biggest, maximum value)
# 6. 'a' will be LCM before, b will be next check number

LCM = 1
GCD = 1
#7. GCD have to be initialize per check number chaged

# check 2
GCD = 1
for i in range(1, 2+1):
    if LCM % i == 0 and 2 % i == 0 and i > GCD:
        GCD = i
LCM = (LCM / GCD) * (2 / GCD) * GCD


# check 3
GCD = 1
for i in range(1, 3+1):
    if LCM % i == 0 and 3 % i == 0 and i > GCD:
        GCD = i
LCM = (LCM / GCD) * (3 / GCD) * GCD

# check 4
GCD = 1
for i in range(1, 4+1):
    if LCM % i == 0 and 4 % i == 0 and i > GCD:
        GCD = i
LCM = (LCM / GCD) * (4 / GCD) * GCD

# check 5
GCD = 1
for i in range(1, 5+1):
    if LCM % i == 0 and 5 % i == 0 and i > GCD:
        GCD = i
LCM = (LCM / GCD) * (5 / GCD) * GCD

# check 6
GCD = 1
for i in range(1, 6+1):
    if LCM % i == 0 and 6 % i == 0 and i > GCD:
        GCD = i
LCM = (LCM / GCD) * (6 / GCD) * GCD

# check 7
GCD = 1
for i in range(1, 7+1):
    if LCM % i == 0 and 7 % i == 0 and i > GCD:
        GCD = i
LCM = (LCM / GCD) * (7 / GCD) * GCD

# 8. enough! this code works lets loop with for
LCM = 1
for j in range(1, 20 + 1):
    GCD = 1
    for i in range(1, j+1): 
        if LCM % i == 0 and j % i == 0 and i > GCD:
            GCD = i
    LCM = (LCM / GCD) * (j / GCD) * GCD

print(GCD, LCM) #232792560