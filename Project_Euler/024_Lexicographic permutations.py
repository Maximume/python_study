# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# 1. permutation? import permutations from itertools!

from itertools import permutations

# 2. our digits are 0~9

digit_list = list(range(0,9+1))

# 3. find permuations and print 1000000th number

perm = list(permutations(digit_list, 10))
print(perm[999999])