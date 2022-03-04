from queue import PriorityQueue
from pyamaze import maze, agent, textLabel, COLOR

def h(cell1 : tuple, cell2 : tuple) -> int:
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def aStar(m, start = None):
    if start is None:
        start = (m.rows, m.cols)

    g_score = {cell : float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell : float('inf') for cell in m.grid}
    f_score[start] = g_score[start] + h(start, m._goal)

    open = PriorityQueue()
    close = PriorityQueue()
    open.put((f_score[start], h(start, m._goal), start))
    
    aPath = {}
    searchPath = [start]

    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)

        if currCell == m._goal:
            break

        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, h(childCell, m._goal), childCell))
                    aPath[childCell] = currCell


    fwdPath = {}
    cell = m._goal

    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]

    return searchPath, aPath, fwdPath

if __name__ == '__main__':
    m = maze(20, 20)
    m.CreateMaze()
    path = aStar(m)

    searchPath, aPath, fwdPath = aStar(m)
    a = agent(m, footprints = True, color = COLOR.blue, filled = True)
    b = agent(m, 1, 1, footprints = True, color = COLOR.yellow, filled = True, goal = (m.rows, m.cols))
    c = agent(m, footprints = True, color = COLOR.red)
    
    m.tracePath({a:searchPath}, delay = 50)
    m.tracePath({b:aPath}, delay = 10)
    m.tracePath({c:fwdPath}, delay = 10)

    l = textLabel(m, 'Astar Path Length', len(fwdPath) + 1)
    l = textLabel(m, 'Astar Search Length', len(searchPath) + 1)

    m.run()