# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# 1. start with duplicate given sequence by code

# n = 13
# print(n)
# while(n != 1):
#     if n%2 == 0:
#         n = n * 0.5
#     else:
#         n = (n * 3) + 1
#     print(n)

# 2. duplication works fine, make loop from 1 to 1,000,000

max_cnt = 0
max_num = 0

for i in range(1,1000000+1):
    cnt = 0
    num = i
    while(i != 1):
        if i%2 == 0:
            i = i * 0.5
        else:
            i = (i * 3) + 1
        cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt
        max_num = num
print(max_num, max_cnt) #837799 524