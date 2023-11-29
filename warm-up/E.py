from copy import copy

n = int(input())
A = list(map(int, input().split()))

prefixes = [0] + copy(A)
for i in range(1, len(A) + 1):
    prefixes[i] = prefixes[i - 1] + A[i - 1]

for i in range(1, len(prefixes)):
    left = A[i - 1] * i - prefixes[i]
    right = prefixes[-1] - prefixes[i] - A[i - 1] * (len(A) - i)
    print(left + right, end=" ")
print()
