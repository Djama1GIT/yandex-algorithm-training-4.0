def permutation(n, prefix, lst):
    if len(prefix) == n:
        yield prefix
    else:
        for i in range(len(lst)):
            prefix.append(lst[i])
            lst.remove(lst[i])
            yield from permutation(n, prefix, lst)
            lst.insert(i, prefix.pop())


N = int(input())
data = list(range(1, N + 1))
for p in permutation(N, [], data):
    print(*p, sep="")
