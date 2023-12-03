def preprocess(s):
    return '#'.join('^{}$'.format(s))


def manacher(s):
    T = preprocess(s)
    n = len(T)
    P = [0] * n
    C = R = 0

    for i in range(1, n - 1):
        i_mirror = 2 * C - i
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0

        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        if i + P[i] > R:
            C, R = i, i + P[i]

    return sum((v + 1) // 2 for v in P)


print(manacher(input()))
