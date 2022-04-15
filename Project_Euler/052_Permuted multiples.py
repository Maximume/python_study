# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

# 1. thus multiple 1 to 6, first digit must be 1

# 2. even n case of multiple 6, digits of origin number and multipled number are same, so answer is under 1.66666 * 10^x

# 3. by 2. instead of checking every numbers, only have to check 10~16, 100~166, 1000~1666, ... and so on.

# 4. make method checking 10~16 and make it general

import time
start = time.time()
checker = 0
d = 2
while checker == 0:
    for n in range(10**(d-1), int(10**d/6) + 1):
        n2 = n * 2
        n3 = n * 3
        n4 = n * 4
        n5 = n * 5
        n6 = n * 6
        str_n1 = str(n)
        str_n2 = str(n2)
        str_n3 = str(n3)
        str_n4 = str(n4)
        str_n5 = str(n5)
        str_n6 = str(n6)
        l_str_n1 = []   # 2 digits
        l_str_n2 = []
        l_str_n3 = []
        l_str_n4 = []
        l_str_n5 = []
        l_str_n6 = []

        for i in range(d):
            l_str_n1.append(str_n1[i])
            l_str_n2.append(str_n2[i])
            l_str_n3.append(str_n3[i])
            l_str_n4.append(str_n4[i])
            l_str_n5.append(str_n5[i])
            l_str_n6.append(str_n6[i])

        l_str_n1.sort()
        l_str_n2.sort()
        l_str_n3.sort()
        l_str_n4.sort()
        l_str_n5.sort()
        l_str_n6.sort()

        if l_str_n1 == l_str_n2 == l_str_n3 == l_str_n4 == l_str_n5 == l_str_n6:
            print(n)
            checker = 1
            break
    d += 1

print (time.time() - start)