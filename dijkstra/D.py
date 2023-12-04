from heapq import heappop, heappush


def dijkstra(adjacency: dict[int, dict[int, list[tuple[int, int]]]], start: int, finish: int) -> int:
    dist = {vertex: float('inf') for vertex in range(len(adjacency))}
    dist[start] = 0

    heap = [(0, start)]
    while heap:
        min_arrive_time, node = heappop(heap)

        for neighbor, times in adjacency[node].items():
            depart_time, arrive_time = float('inf'), float('inf')
            for time in times:
                if time[0] >= min_arrive_time and arrive_time > time[1]:
                    depart_time, arrive_time = time
            new_arrive_time = arrive_time
            if new_arrive_time < dist[neighbor]:
                dist[neighbor] = new_arrive_time
                heappush(heap, (new_arrive_time, neighbor))

    return dist[finish] if dist[finish] != float('inf') else -1


n = int(input())
d, v = map(int, input().split())
r = int(input())

edges = {}

for i in range(n):
    edges[i] = {}

for i in range(r):
    from_village_num, leave, to_village_num, arrive = map(int, input().split())
    if not to_village_num - 1 in edges[from_village_num - 1]:
        edges[from_village_num - 1][to_village_num - 1] = []
    edges[from_village_num - 1][to_village_num - 1] += [(leave, arrive)]

print(dijkstra(edges, d - 1, v - 1))
