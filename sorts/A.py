def partition(arr, pivot):
    i = 0
    for j in range(len(arr)):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i


N = int(input())
array = list(map(int, input().split()))
x = int(input())
pivotIndex = partition(array, x)
print(pivotIndex)
print(len(array) - pivotIndex)
