from heapq import heappop, heappush


def dijkstra(adjacency, start, finish):
    dist = {vertex: float('inf') for vertex in range(len(adjacency))}
    dist[start] = 0

    heap = [(0, start)]
    while heap:
        min_distance, node = heappop(heap)

        for neighbor, weight in adjacency[node].items():
            new_distance = dist[node] + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                heappush(heap, (new_distance, neighbor))

    return dist[finish] if dist[finish] != float('inf') else -1


n, k = map(int, input().split())

edges = {}
for i in range(n):
    edges[i] = {}
for i in range(k):
    a, b, l = map(int, input().split())
    edges[a - 1][b - 1] = l
    edges[b - 1][a - 1] = l

a, b = map(int, input().split())

print(dijkstra(edges, a - 1, b - 1))
