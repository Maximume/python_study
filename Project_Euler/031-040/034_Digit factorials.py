# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# 1. to find searching range, maximum value of single digit factorial is needed

# digit_max_fac = 1
# for i in range(1, 9+1):
#     digit_max_fac *= i
# print(digit_max_fac) # 362880

# 2. if there is 7 digits number full of nines, sum of single digit factorial is 362880 * 7

# 3. 9999999 > 2540160

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

ans_list = []
for i in range(3, 10000000):
    str_i = str(i)
    sum = 0
    for j in str_i:
        sum += fact(int(j))
    if i == sum:
        ans_list.append(i)

for i in ans_list:
    print(i)

sum = 0
for i in ans_list:
    sum += i
print(i)