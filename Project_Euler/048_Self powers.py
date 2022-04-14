# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# 1. it seems easy. check out it works as I thought
import time
start = time.time()
sum = 0
for i in range(1, 1000 +1):
    sum += i ** i

print(str(sum)[-10:]) #9110846700
end = time.time()
operation_time = end - start
print(operation_time)
# 2. it works...