l0 = [
    [[0, 0, 0]]
]

l1 = [ #D1 =1
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
]

l2 = [  #D2 = 3
    [[0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0], [2, 0, 0]],
    [[0, 0, 1], [0, 1, 1], [0, 2, 0], [1, 0, 0], [1, 1, 0]],
    [[0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1]]
]

l3 = [  #D3 = 9        # 이동이 가능한지 먼저 체크
    [[0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 0], [2, 0, 1], [2, 1, 0], [3, 0, 0]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 1], [1, 1, 1], [1, 2, 0], [2, 0, 0], [2, 1, 0]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 2], [1, 1, 0], [1, 1, 1], [2, 0, 0], [2, 0, 1]],
    [[0, 0, 1], [0, 1, 1], [0, 2, 0], [1, 0, 0], [1, 1, 1], [1, 2, 0], [2, 1, 0]],
    [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 0], [1, 0, 0], [1, 1, 0], [1, 2, 0]],
    [[0, 0, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [1, 0, 0], [1, 1, 0], [1, 1, 1]],
    [[0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 2], [1, 1, 1], [2, 0, 1]],
    [[0, 0, 2], [0, 1, 0], [0, 1, 2], [0, 2, 1], [1, 0, 0], [1, 0, 1], [1, 1, 1]],
    [[0, 0, 3], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2]]
]

# for i in l4:
#     i.sort()
# l4.sort()

# for i in l4:
#     print(i)