import collections
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
    q = collections.deque([i])
    while q:
        num = q.popleft()
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

"""
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <limits>

class City {
public:
   int num;
   int waitTime;
   int speed;

   City() : num(0), waitTime(0), speed(0) {}
   City(int num, int waitTime, int speed) : num(num), waitTime(waitTime), speed(speed) {}
};


class Road {
public:
    int startNum;
    int finishNum;
    int distance;

    Road(int startNum, int finishNum, int distance) : startNum(startNum), finishNum(finishNum), distance(distance) {}
};

class CitiTime {
public:
    int num;
    double time;

    CitiTime(int num, double time) : num(num), time(time) {}

    bool operator<(const CitiTime &other) const {
        return time > other.time;
    }
};

std::vector<City> cities;
std::unordered_map<int, std::vector<Road>> roadMap;
std::vector<std::vector<double>> timeMatrix;
std::vector<double> minTime;
std::vector<int> prev;

void calculate();
std::string getPath(int from);
int getMaxPos(const std::vector<double> &doubles);
void build();
void init();

int main() {
    init();
    build();
    calculate();
    return 0;
}

void calculate() {
    minTime = std::vector<double>(cities.size(), std::numeric_limits<double>::max());
    prev = std::vector<int>(cities.size(), 1);
    prev[0] = 0;
    prev[1] = -1;
    std::copy(timeMatrix[1].begin(), timeMatrix[1].end(), minTime.begin());
    std::priority_queue<CitiTime> queue;
    for (int i = 1; i < cities.size(); i++) {
        queue.push(CitiTime(i, minTime[i]));
    }
    while (!queue.empty()) {
        CitiTime citiTime = queue.top();
        queue.pop();
        for (int i = 1; i < cities.size(); i++) {
            double newTime = citiTime.time + timeMatrix[citiTime.num][i];
            if (newTime < minTime[i]) {
                minTime[i] = newTime;
                queue.push(CitiTime(i, newTime));
                prev[i] = citiTime.num;
            }
        }
    }
    int maxPos = getMaxPos(minTime);
    std::cout.precision(10);
    std::cout << minTime[maxPos] << std::endl;
    std::cout << getPath(maxPos) << std::endl;
}

std::string getPath(int from) {
   std::string path;
   for (int i = from; i != -1; i = prev[i]) {
       path += std::to_string(i) + " ";
   }
   path.pop_back();
   return path;
}


int getMaxPos(const std::vector<double> &doubles) {
    int pos = 1;
    double max = doubles[pos];
    for (int i = 2; i < doubles.size(); i++) {
        if (doubles[i] > max) {
            max = doubles[i];
            pos = i;
        }
    }
    return pos;
}

void build() {
    std::vector<std::vector<int>> distanceMatrix(cities.size(), std::vector<int>(cities.size(), -1));
    for (int i = 1; i < cities.size(); i++) {
        distanceMatrix[i][i] = 0;
        std::queue<int> q;
        q.push(i);
        while (!q.empty()) {
            int num = q.front();
            q.pop();
            for (const auto &road : roadMap[num]) {
                if (distanceMatrix[i][road.finishNum] == -1) {
                    distanceMatrix[i][road.finishNum] = distanceMatrix[i][road.startNum] + road.distance;
                    q.push(road.finishNum);
                }
            }
        }
    }
    timeMatrix = std::vector<std::vector<double>>(cities.size(), std::vector<double>(cities.size(), std::numeric_limits<double>::max()));
    for (int i = 1; i < cities.size(); i++) {
        for (int j = 1; j < cities.size(); j++) {
            timeMatrix[i][j] = i == j ? 0 : cities[j].waitTime + static_cast<double>(distanceMatrix[i][j]) / cities[j].speed;
        }
    }
}

void init() {
   int n;
   std::cin >> n;
   cities = std::vector<City>(n + 1);
   for (int i = 1; i < n + 1; i++) {
       int t, v;
       std::cin >> t >> v;
       cities[i] = City(i, t, v);
   }
   roadMap = std::unordered_map<int, std::vector<Road>>(n);
   for (int i = 0; i < n - 1; i++) {
       int s, f, d;
       std::cin >> s >> f >> d;
       roadMap[s].push_back(Road(s, f, d));
       roadMap[f].push_back(Road(f, s, d));
   }
}

"""