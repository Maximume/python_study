import heapq

graph = {
    'A' : {'B' : 10, 'C' : 30, 'D' : 15},
    'B' : {'E' : 20},
    'C' : {'F' : 5},
    'D' : {'C' : 5, 'F' : 20},
    'E' : {'F' : 20},
    'F' : {'D' : 20}
}

def dijkstra(graph, start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    path = {
        'A' : [],
        'B' : [],
        'C' : [],
        'D' : [],
        'E' : [],
        'F' : []
    }
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                path[new_destination].append(current_destination)
                heapq.heappush(queue, [distance, new_destination])
    print(path)
    print(distances)
    return distances

dijkstra(graph, 'A')