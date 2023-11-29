a = int(input())
b = int(input())
n = int(input())

print(["Yes", "No"][a <= b // n + (b % n != 0)])
