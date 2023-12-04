def dijkstra(adjacency, start, finish):
    dist = {vertex: float('inf') for vertex in range(len(adjacency))}
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

    return dist[finish] if dist[finish] != float('inf') else -1


n, s, f = map(int, input().split())

edges = {}

for i in range(n):
    edges[i] = {}
    for idx, j in enumerate(map(int, input().split())):
        if j != -1:
            edges[i][idx] = j

print(dijkstra(edges, s - 1, f - 1))
