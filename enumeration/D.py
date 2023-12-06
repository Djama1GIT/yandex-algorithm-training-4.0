def shortest_path(n, g):
    visited = [False] * n
    visited[0] = True
    min_path = find_path(n, g, visited, 1, 0, 0)
    min_path = min_path if min_path != float('inf') else -1
    return min_path


def find_path(n, g, visited, visited_count, visited_length, last_visited):
    if n == 1:
        return 0

    if visited_count == n:
        edge = g[last_visited][0]
        return float('inf') if edge == 0 else (edge + visited_length)

    length = float('inf')
    for i in range(n):
        edge = g[last_visited][i]
        if edge != 0 and not visited[i]:
            visited[i] = True
            l = find_path(n, g, visited, visited_count + 1, visited_length + edge, i)
            length = min(length, l)
            visited[i] = False
    return length


n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))
min_cycle = shortest_path(n, g)
print(min_cycle)
