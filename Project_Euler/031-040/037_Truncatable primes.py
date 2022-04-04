# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def check_ltr(n):
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[1:]
        if not int(str_n) in prime_list:
            return False
    return True
def check_rtl(n):
    str_n = str(n)
    while len(str_n) > 1:
        str_n = str_n[:-1]
        if not int(str_n) in prime_list:
            return False
    return True

n = 1000000

trun_primes = []

a = [False, False] + [True] * (n-1)
prime_list = []

for i in range(2, n+1):
    if a[i]:
        prime_list.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

for i in prime_list:
    if check_ltr(i) and check_rtl(i) and i > 10:
        trun_primes.append(i)
print(trun_primes, len(trun_primes))    #[23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397] 11

sum = 0
for i in trun_primes:
    sum += i

print(sum)  #748317