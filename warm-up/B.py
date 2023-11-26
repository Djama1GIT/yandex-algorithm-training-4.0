from math import gcd

a, b, c, d = map(int, input().split())
n = b * d
m = a * d + b * c

_gcd = gcd(n, m)

print(m // _gcd, n // _gcd)
