# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?

# 1. thus right alngle triangle, a^2 + b^2 = c^2
# 2. only combinations are need, let's assume a < b < c
# 3. so, a is less than p/3, b is less than p/2
# 4. if a , b and p is given, c = p - a - b

lists = []
for p in range(0, 1000):    #if p = 1000, there is only one triplet
    print("checking ", p)
    cnt = 0
    for a in range(1, int(p/3)):
        for b in range(a, int(p/2)):
            if a+b>p/2:
                pass
            if a**2 + b**2 == (p -a -b)**2:
                cnt += 1
    lists.append(cnt)

print(lists.index(max(lists)))  #840