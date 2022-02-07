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
