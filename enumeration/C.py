def cut(connected, current_sum, current_combination, maximum_combination):
    if connected == N:
        return current_sum
    else:

        current_combination[connected] = True
        sum1 = current_sum
        for B in range(connected):
            if current_combination[connected] != current_combination[B]:
                sum1 += G[connected][B]
        max_combination1 = current_combination.copy()
        sum1 = cut(connected + 1, sum1, current_combination, max_combination1)

        current_combination[connected] = False
        sum2 = current_sum
        for B in range(connected):
            if current_combination[connected] != current_combination[B]:
                sum2 += G[connected][B]
        max_combination2 = current_combination.copy()
        sum2 = cut(connected + 1, sum2, current_combination, max_combination2)

        if sum1 > sum2:
            maximum_combination[:] = max_combination1
        else:
            maximum_combination[:] = max_combination2
        return max(sum1, sum2)


N = int(input())
G = [[0] * N for _ in range(N)]
for i in range(N):
    G[i] = list(map(int, input().split()))

cur_combination = [False] * N
max_combination = [False] * N
max_result = cut(0, 0, cur_combination, max_combination)

print(max_result)
for i in range(N):
    print(1 if max_combination[i] else 2, end=' ')
print()
