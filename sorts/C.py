def merge(arr1, arr2):
    arr3 = []

    i1 = 0
    i2 = 0

    while len(arr3) != len(arr1) + len(arr2):
        if i1 == len(arr1):
            arr3 += [arr2[i2]]
            i2 += 1
        elif i2 == len(arr2):
            arr3 += [arr1[i1]]
            i1 += 1
        elif arr1[i1] < arr2[i2]:
            arr3 += [arr1[i1]]
            i1 += 1
        else:
            arr3 += [arr2[i2]]
            i2 += 1

    return arr3


input()
a1 = list(map(int, input().split()))
input()
a2 = list(map(int, input().split()))

print(*merge(a1, a2))
