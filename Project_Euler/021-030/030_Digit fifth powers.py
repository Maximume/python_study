# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# 1. for find number range first, calculate 9^5 the biggest value from digit

# check = 9**5
# print(check) #59049

# 2. to make 59049, number needs 5digits, but 5 * (9**5) needs 6digits

# 3. so, our maximum range will be 59049 * 6 = 354294 and 354294 doesnt pit our condition

ran = list(range(2, 354294))
checked_list = []
for i in ran:
    str_i = str(i)
    sum = 0
    for j in str_i:
        sum += int(j)**5
    if i == sum:
        checked_list.append(i)

print(checked_list) #[4150, 4151, 54748, 92727, 93084, 194979]
res = 0
for i in checked_list:
    res += i
print(res)  #443839