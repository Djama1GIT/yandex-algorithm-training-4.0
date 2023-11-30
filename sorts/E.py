import copy
from collections import defaultdict


def print_phase(bucks):
    for i in range(10):
        print(f"Bucket {i}: ", end="")
        if bucks[i]:
            print_bucket(bucks[i])
        else:
            print("empty")
    print("**********")


def print_bucket(bucket):
    [print(f"{bucket[i]}, ", end="") for i in range(len(bucket) - 1)]
    print(f"{bucket[-1]}")


array = [input() for _ in range(int(input()))]
print("Initial array:")
print_bucket(array)
print("**********")

buckets = defaultdict(list)

for i in array:
    buckets[int(i[-1])] += [i]
print("Phase 1")
print_phase(buckets)

for phase in range(1, len(array[0])):
    _buckets = defaultdict(list)
    for bucket in range(10):
        for i in range(len(buckets[bucket])):
            _buckets[int(buckets[bucket][i][-phase - 1])] += [buckets[bucket][i]]
    buckets = _buckets
    print("Phase", phase + 1)
    print_phase(buckets)

print("Sorted array:")

result = ""
for i in range(10):
    if buckets[i]:
        result += "".join([f"{buckets[i][j]}, " for j in range(len(buckets[i]) - 1)])
        result += f"{buckets[i][-1]}, "
print(result[:-2])
print(result[:-2])
