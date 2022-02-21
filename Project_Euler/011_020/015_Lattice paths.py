# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# 1. it's familiar question, pathfinding, number of cases
# 2. init list with fill with 1
# 3. cases to (x,y) is sum of cases to (x-1,y) and cases to (x,y-1)
# 4. 20x20 grid has 21x21 points each axis
n = 21
arr = [[1]*n for _ in range(n)]

# for i in arr:   #checking list
#     print(i)

for y, line in enumerate(arr):
    for x, number in enumerate(line):
        if x > 0 and y > 0:
            arr[y][x] = arr[y-1][x] + arr[y][x-1]

for i in arr:   #checking list
    print(i)
print(arr[20][20])  #137846528820