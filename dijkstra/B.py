def dijkstra(adjacency, start, finish):
    dist = {vertex: float('inf') for vertex in range(len(adjacency))}
    prev = {vertex: None for vertex in range(len(adjacency))}
    dist[start] = 0
    visited = set()

    while len(visited) != len(adjacency):
        min_distance = float('inf')
        next_node = None

        for node in range(len(adjacency)):
            if node not in visited and dist[node] < min_distance:
                min_distance = dist[node]
                next_node = node

        if next_node is None:
            break

        visited.add(next_node)

        for neighbor, weight in adjacency[next_node].items():
            new_distance = dist[next_node] + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                prev[neighbor] = next_node

    if dist[finish] != float('inf'):
        path = [finish]
        while path[-1] != start:
            path.append(prev[path[-1]])
        path = path[::-1]
        for idx in range(len(path)):
            path[idx] += 1
        return *path,
    else:
        return -1,


n, s, f = map(int, input().split())

edges = {}

for i in range(n):
    edges[i] = {}
    for idx, j in enumerate(map(int, input().split())):
        if j != -1:
            edges[i][idx] = j

print(*dijkstra(edges, s - 1, f - 1))
