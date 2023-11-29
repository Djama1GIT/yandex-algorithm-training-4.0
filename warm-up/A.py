N, M = map(int, input().split())
n = tuple(map(int, input().split()))

for i in range(M):
    l, r = map(int, input().split())
    _min = 99999999999999999
    __min = 99999999999999999

    for idx in range(l, r + 1):
        if n[idx] < _min:
            __min = _min
            _min = n[idx]
        elif _min != n[idx] < __min:
            __min = n[idx]

    print(__min if _min != __min != 99999999999999999 else "NOT FOUND")

