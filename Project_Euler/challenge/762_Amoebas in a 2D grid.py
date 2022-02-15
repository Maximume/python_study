# Consider a two dimensional grid of squares. The grid has 4 rows but infinitely many columns.

# An amoeba in square (x,y) can divide itself into two amoebas to occupy the squares (x+1,y) and (x+1,y+1 mod4), provided these squares are empty.

# The following diagrams show two cases of an amoeba placed in square A of each grid. When it divides, it is replaced with two amoebas, one at each of the squares marked with B:

# (skip diagrams)

# Originally there is only one amoeba in the square (0,0). After N divisions there will be N+1 amoebas arranged in the grid. An arrangement may be reached in several different ways but it is only counted once. Let C(N) be the number of different possible arrangements after N divisions.

# For example, C(2)=2, C(10)=1301, C(20)=5895236 and the last nine digits of C(100) are 125923036.

# Find C(100000), enter the last nine digits as your answer.

ln = [
[[0,0]]
]

for i in range(20):
    ln_1 = []
    for case in ln:
        for coord in case:
            temp_case = case[:]
            temp_case.remove(coord)
            coord_yp = (coord[1]+1)%4
            modified0 = [coord[0]+1, coord[1]]
            modified1 = [coord[0]+1, coord_yp]
            if modified0 in temp_case or modified1 in temp_case:
                pass
            else:
                temp_case.append(modified0)
                temp_case.append(modified1)
                temp_case.sort()
                if temp_case in ln_1:
                    pass
                else:
                    ln_1.append(temp_case)
    ln = ln_1[:]
    print('C', i+1, ' : ', len(ln_1))

    # for j in ln:
    #     print(j)