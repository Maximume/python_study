# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

# 1. make function that check input number(str type) is palindromic or not

def check_pal(str_i:str) -> bool:
    while len(str_i) > 2:
        if str_i[0] != str_i[-1]:
            return False
        else:
            str_i = str_i[1:-1]
    if str_i[0] != str_i[-1]:
        return False
    return True

# 2. check every numbers under 1000000

sum = 0
for i in range(1, 1000000):
    str_d = str(i)
    str_b = str(bin(i))[2:]
    if check_pal(str_d) and check_pal(str_b):
        sum += i
print(sum)  #872187