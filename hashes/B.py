def prefix_function(s):
    prefix = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = prefix[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix[i] = j
    return prefix


def solve(s):
    prefix = prefix_function(s)
    n = len(s)
    k = prefix[-1]
    return n - k


s = input()
print(solve(s))
