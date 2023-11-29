for i in range(int(input())):
    n, a, b = map(int, input().split())
    if n % a == 0 or n % b == 0:
        print("YES")
    else:
        print("YES" if (n // b + 1) * a <= n else "NO")
