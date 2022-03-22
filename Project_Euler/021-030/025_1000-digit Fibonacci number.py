# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# 1. how to know digits? make to str, check index

# 2. keep append f_list till find f(n) contain 1000 digits
f_list = [1, 1]

n = 2
while True:
    f_n = f_list[n-2] + f_list[n-1]

    ls = len(str(f_n))
    if ls == 1000:
        print(n+1)
        break

    f_list.append(f_n)
    n += 1