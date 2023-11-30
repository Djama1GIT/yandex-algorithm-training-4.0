import random
import sys

sys.setrecursionlimit(2147000000)


def quick_sort(arr, left, right):
    if left + 1 >= right:
        return
    e = left
    g = left
    pivot = arr[random.randint(left, right - 1)]
    for n in range(left, right):
        if arr[n] > pivot:
            continue
        elif arr[n] == pivot:
            arr[g], arr[n] = arr[n], arr[g]
        else:
            arr[n], arr[g] = arr[g], arr[n]
            arr[g], arr[e] = arr[e], arr[g]

            e += 1
        g += 1
    quick_sort(arr, left, e)
    quick_sort(arr, g, right)


input()
array = list(map(int, input().split()))
quick_sort(array, 0, len(array))
print(*array)

