# Consider a three dimensional grid of cubes. An amoeba in cube (x, y, z) can divide itself into three amoebas to occupy the cubes (x+1, y, z), (x, y+1, z) and (x, y, z+1), provided these cubes are empty.

# Originally there is only one amoeba in the cube(0, 0, 0) . After N divisions there will be 2N+1 amoebas arranged in the grid. An arrangement may be reached in several different ways but it is only counted once. Let D(N) be the number of different possible arrangements after N divisions.

# For example, D(2)=3, D(10)=44499, D(20)=9204559704 and the last nine digits of D(100) are 780166455.

# Find D(10000), enter the last nine digits as your answer.

# 1. check given example and make it sure approach and method is right

ln = [ # n = 0
[[0, 0, 0]]
]

for i in range(10000):
    ln_1 = []
    for case in ln:
        for coord in case:
            temp_case = case[:]
            temp_case.remove(coord)
            modified0 = [coord[0]+1, coord[1], coord[2]]
            modified1 = [coord[0], coord[1]+1, coord[2]]
            modified2 = [coord[0], coord[1], coord[2]+1]
            if modified0 in temp_case or modified1 in temp_case or modified2 in temp_case:
                pass
            else:
                temp_case.append(modified0)
                temp_case.append(modified1)
                temp_case.append(modified2)
                temp_case.sort()
                if temp_case in ln_1:
                    pass
                else:
                    ln_1.append(temp_case)
    ln = ln_1[:]
    print('D', i+1, ' : ', len(ln_1))

# 2. D(10) =44499 is printed out by this method
# 3. but, takes too much time even just calculate to D(10)
# 4. other solution or algorithm for shorten calculation is needed


