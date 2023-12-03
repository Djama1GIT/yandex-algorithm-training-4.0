s = input()
n = len(s)
p = 10 ** 9 + 7
x_ = 499
h = [0] * (n + 1)
x = [0] * (n + 1)
x[0] = 1
s = ' ' + s
for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(s[i])) % p
    x[i] = (x[i - 1] * x_) % p


def chavo(_len, _from1, _from2):
    return (h[_from1 + _len - 1] + h[_from2 - 1] * x[_len]) % p == (
            h[_from2 + _len - 1] + h[_from1 - 1] * x[_len]) % p


for i in range(int(input())):
    l, a, b = map(int, input().split())
    print("yes" if chavo(l, a + 1, b + 1) else "no")
