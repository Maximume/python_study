# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools
import time

start = time.time()
l1 = []
for i in range(0, 10):
    str_i = str(i)
    l1.append(str_i)

str_per = list(map(''.join, itertools.permutations(l1)))

checker = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}

checked = []

for per in str_per:
    if per[0] == '0':
        check_0 = 1
    else:
        check_0 = 0
    num_check = 0
    for idx in checker.keys():
        if int(per[idx+check_0:idx+check_0+3]) % checker[idx] != 0:
            num_check += 1
    if num_check == 0:
        checked.append(per)
print(checked)  #['1406357289', '1430952867', '1460357289', '4106357289', '4130952867', '4160357289']

sum = 0
for i in checked:
    sum += int(i)
print(sum)  #16695334890


    

end = time.time()
print(end-start)