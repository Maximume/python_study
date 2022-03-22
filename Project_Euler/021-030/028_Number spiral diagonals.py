# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# 1. to find regularity of a sequence, group 4 numbers which are in edges

#   [1], [3, 5, 7, 9], [13, 17, 21, 25], [31, 37, 43, 49], [57, 65, 73, 81]

# 2. general term of last number of each group can be (2n+1)^2 when ignore [1]

# 3. then, sum of each group will be, 4(2n+1)^2-2n-4n-6n = 16n^2 + 4n + 4

# 4. thus 1 is ignored and each group contains 4 numbers, to find diagonals in a 1001 by 1001 n will be 500

sum = 1

for n in range(1, 500 + 1):
    sum += 16*(n**2) + (4 * n) + 4
print(sum)
