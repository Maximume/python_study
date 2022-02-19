# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

#    3
#   7 4
#  2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

#               75
#              95 64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

# 1. make the triangle to list, as t_list[i][j]

numbers = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
splited_numbers = numbers.split('\n')
t_list = []
for i in splited_numbers:
    t_list.append(i.split())

# 2. to make calculate easier, make every arguments in t_list into int

for i, line in enumerate(t_list):
    for j, num in enumerate(line):
        t_list[i][j] = int(t_list[i][j])

# 3. if case reach to '63' in t_list[13][0], to make total biggest t_list[14][x] must be t_list[14][1] which is '62' not t_list[14][0] (04)
# 4. by this regulation, replacing t_list[13][0] to sum of t_list[13][0] and t_list[14][1] doesn't make any change to calculate biggest total
# 5. by this method, only takes 105 comparing two numbers and 105 adding calculations needed

# replacing t_list[13][0]
# if t_list[13+1][0+0] > t_list[13+1][0+1]:
#     t_list[13][0] = t_list[13][0] + t_list[13+1][0+0]
# else:
#     t_list[13][0] += t_list[13+1][0+1]

# for i in t_list:
#     print(i)    #t_list[13][0] replaced by 125 (63 + 62)

# 6. make this method for every arguments in row13

# for i, num in enumerate(t_list[13]):
#     if t_list[13+1][i+0] > t_list[13+1][i+1]:
#         t_list[13][i] = t_list[13][i] + t_list[13+1][i+0]
#     else:
#         t_list[13][i] += t_list[13+1][i+1]

# for i in t_list:
#     print(i)    #every arguments in t_list[13] replaced

# 7. next step is checking t_list[12]

# for i, num in enumerate(t_list[12]):
#     if t_list[12+1][i+0] > t_list[12+1][i+1]:
#         t_list[12][i] = t_list[12][i] + t_list[12+1][i+0]
#     else:
#         t_list[12][i] += t_list[12+1][i+1]

# 8. make it loop 13, 12, 11, ..., 3, 2, 1, 0
for j in reversed(range(1,len(t_list)-1)):
    for i, num in enumerate(t_list[j]):
        if t_list[j+1][i+0] > t_list[j+1][i+1]:
            t_list[j][i] = t_list[j][i] + t_list[j+1][i+0]
        else:
            t_list[j][i] += t_list[j+1][i+1]

for i in t_list:
    print(i)

# 9. remained list [75], [995, 999]