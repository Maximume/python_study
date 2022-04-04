# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

# 1. first, we need to know prime numbers below one million

# n = 1000000

# a = [False, False] + [True] * (n-1)
# prime_list = []

# for i in range(2, n+1):
#     if a[i]:
#         prime_list.append(i)
#         for j in range(2*i, n+1, i):
#             a[j] = False

# 2. every digits has chance to be 10^0 decimal point, so even number is included, prime number cannot be circular prime

def check_digit(str_i:str)->bool:
    for i in str_i:
        if int(i) % 2 == 0 or int(i) % 5 == 0:
            return False
    return True

n = 1000000

a = [False, False] + [True] * (n-1)
prime_list = []

for i in range(2, n+1):
    if a[i]:
        str_i = str(i)
        if check_digit(str_i):
            prime_list.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

# 3. if our prime number made of 6 digits, for example abcdef, rotations will be bcdefa, cdefab, defabc, efabcd, fabcde. It means handle this number as str, value of index 0 will append to index -1 for n-1 time(n digits)

def check_circular(rotates:list) -> bool:
    for i in rotates:
        if not i in prime_list:
            return False
    return True


circular_primes = []
for i in prime_list:
    str_i = str(i)

    k = 0
    rotates = []
    while k < len(str_i):
        str_i = str_i[1:]+str_i[0]
        rotates.append(int(str_i))
        k += 1
    rotates = list(set(rotates))
    if check_circular(rotates):
        circular_primes += rotates

print(len(set(circular_primes)) + 2)    # +2 because 2, 5
# 55