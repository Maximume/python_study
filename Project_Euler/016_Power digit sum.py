# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# 1. calculate target number

target_number = 2 ** 1000
# 2. make it str type so that can calculate with indexing

str_number = str(target_number)

sum = 0
for i in str_number:
    sum += int(i)
print(sum)

# 3. dynamic typing of python make it easy!