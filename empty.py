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