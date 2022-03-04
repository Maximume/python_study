def fib(n):
    r5 = 5 ** 0.5
    fib_n = (((1 + r5) / 2) ** n - ((1 - r5) / 2) ** n) / r5
    print(fib_n)
    return fib_n

a = fib(1000)

fl = [1, 1]

for i in range(2, 1000000 + 1):
    fi = fl[i-1] + fl[i-2]
    fl.append(fi)
print(fl[-2])