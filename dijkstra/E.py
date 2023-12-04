import heapq

n = int(input())
cities = [[]] * (n + 1)
for i in range(1, n + 1):
    t, v = map(int, input().split())
    cities[i] = [i, t, v]  # num, wait_time, speed

road_map = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    s, f, d = map(int, input().split())
    road_map[s].append([s, f, d])  # start_num, finish_num, distance
    road_map[f].append([f, s, d])  # start_num, finish_num, distance

distance_matrix = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    distance_matrix[i][i] = 0
    q = [i]
    while q:
        num = q.pop(0)
        for road in road_map[num]:
            if distance_matrix[i][road[1]] == -1:
                distance_matrix[i][road[1]] = distance_matrix[i][road[0]] + road[2]
                q.append(road[1])

time_matrix = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            time_matrix[i][j] = 0
        else:
            time_matrix[i][j] = cities[j][1] + distance_matrix[i][j] / cities[j][2]

min_time = [time_matrix[1][i] for i in range(n + 1)]
prev = [1] * (n + 1)
prev[0] = 0
prev[1] = -1
queue = [(min_time[i], i) for i in range(1, n + 1)]
heapq.heapify(queue)

while queue:
    time, num = heapq.heappop(queue)
    for i in range(1, n + 1):
        new_time = time + time_matrix[num][i]
        if new_time < min_time[i]:
            min_time[i] = new_time
            heapq.heappush(queue, (new_time, i))
            prev[i] = num

max_pos = max(range(2, n + 1), key=lambda i: min_time[i])
path = []
while max_pos != -1:
    path.append(max_pos)
    max_pos = prev[max_pos]

print(f'{min_time[path[0]]:.10f}')
print(' '.join(map(str, path)))