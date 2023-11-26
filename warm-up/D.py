from collections import Counter

a = Counter(input())
b = Counter(input())

flag = True
for char in b:
    if a.get(char, 0) < b.get(char, 0):
        flag = False
        break

flag2 = True
for char in a:
    if b.get(char, 0) < a.get(char, 0):
        flag2 = False
        break

print("YES" if (flag or flag2) else "NO")
