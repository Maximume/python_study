# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

# 1. thus n > 1, minimum list of (1,2, ... , n) will be (1, 2)

# 2. if minimum list of (1,2, ... , n) was (1, 2), multipled number has 4 digits, under 9999

# 3. Since the value multipled by 1 is added first, check reverse order will be better

import time
start = time.time()

largest = 0

for i in range(9999, 0, -1):
    str_num = ''
    j = 1
    while len(str_num) < 9:
        str_num += str(i*j)
        j += 1
        if len(str_num) == 9 and set(str_num) == set('123456789') and int(str_num) > largest:
            largest = int(str_num)

end = time.time()
print(largest)
print(end-start)