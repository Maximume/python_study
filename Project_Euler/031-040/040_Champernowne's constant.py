# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789 101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import time

start = time.time()

str_num = '0'
i = 1
while len(str_num) < 1000000:
    str_num += str(i)
    i += 1

idx = 1
ans = 1

while idx < len(str_num):
    ans *= int(str_num[idx])
    idx *= 10

end = time.time()
print(ans)
print(end - start)
