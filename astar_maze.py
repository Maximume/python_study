import os
import time

f = open('maze_map.txt', 'r')

maze = f.readlines()
for lines in range(len(maze)):
    maze[lines] = maze[lines].split()

start = (8, 0)
end = (0, 8)

class Node:
    def __init__(self, parent = None, position = None) -> None:
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def heuristic(node, goal) -> int:
    dx = abs(node.position[0] - goal.position[0])
    dy = abs(node.position[1] - goal.position[1])
    return dx + dy

def aStar() -> list:
    startNode = Node(None, start)
    endNode = Node(None, end)

    openList = [startNode]
    closedList = []

    while openList:
        currentNode = openList[0]

        for idx, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item

        openList.remove(currentNode)
        closedList.append(currentNode)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                x, y = current.position
                maze[x][y] = '@'
                path.append(current.position)
                current = current.parent
            return path[::-1]

        for newPosition in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

            nodePosition = (
                currentNode.position[0] + newPosition[0],
                currentNode.position[1] + newPosition[1])
                
            within_range_criteria = [
                nodePosition[0] > (len(maze) - 1),  #rows range
                nodePosition[0] < 0,
                nodePosition[1] > (len(maze[0]) - 1),   #col range
                nodePosition[1] < 0,
            ]

            if any(within_range_criteria):
                continue

            # block check
            if maze[nodePosition[0]][nodePosition[1]] == 'x':
                continue

            new_node = Node(currentNode, nodePosition)
            nx, ny = new_node.position
            maze[nx][ny] = '#'

            if new_node in closedList:
                continue

            for line in maze:
                for tile in line:
                    print(tile, end = ' ')
                print()

            time.sleep(0.0001)
            os.system('cls')

            new_node.g = currentNode.g + 1
            new_node.h = heuristic(new_node, endNode)
            new_node.f = new_node.g + new_node.h

            if len([openNode for openNode in openList if new_node == openNode and new_node.g > openNode.g]) > 0:
                continue
                    
            openList.append(new_node)

def main():
    os.system('cls')
    path = aStar()

    for line in maze:
        for tile in line:
            print(tile, end = ' ')
        print()
main()