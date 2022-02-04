# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# 1. for calculate index I need to know range 100 * 100 to 999 * 999

min = 100 * 100
max = 999 * 999 #min 10000, max 998001

# 2. number of digits of min and max is not same. so divide range by 10000 ~ 99999, 100000 ~ 998001
# 3. combination number doesn't have to be same numbers
# 4. number of digits of min and max is not same. but still they are 5~6digits
# 5. It means I can compare [0],[-1], [1],[-2] regardless digits
# 6. How can I make target numbers?
# 7. list all of 100~999 * 100~999 and remove duplications? this process need 810000 calculations

target_numbers = []
for i in range(100, 999):
    for j in range(100, 999):
        target_numbers.append(i*j)

target_numbers = sorted(list(set(target_numbers)))
# # print(len(target_numbers)) #227152

# 8. number of target numbers is 227152. not too many. Now checking palindromic numbers by index
# 9. int doesn't have index, so make it str. then I can check digits by checking index

filtered_numbers = []
for k in target_numbers:
    if (str(k)[0] == str(k)[-1]) and (str(k)[1] == str(k)[-2]) and (str(k)[2] == str(k)[-3]):
        filtered_numbers.append(k)
print(filtered_numbers) 

# 10. numbers of palindromic numbers are 655, largest palindrome made from the product of two 3-digit numbers is 906609

# 11. but I don't know combination of 906609. Let's trace back when 906609 is generated

for i in range(100, 999):
    for j in range(100, 999):
        if i*j == 906609:
            print (i,j)
            break       #913, 993

# 12. largest palindrome made from the product of two 3-digit numbers is 906609, and combination is (913, 993)