from math import atan2, hypot, pi, degrees

xA, yA, xB, yB = map(int, input().split())


def moscow(x1, y1, x2, y2) -> float:
    def straight_distance(_x1, _y1, _x2, _y2):
        return hypot(_x2 - _x1, _y2 - _y1)

    def circle_distance(alpha, beta, radius):
        alpha = degrees(alpha)
        beta = degrees(beta)
        alpha, beta = min(alpha, beta), max(alpha, beta)
        return (pi * radius * (beta - alpha)) / 180

    first = straight_distance(x1, y1, 0, 0)
    second = straight_distance(x2, y2, 0, 0)
    second, first = max(first, second), min(first, second)
    var1 = first + second

    var2 = second - first + circle_distance(atan2(y2, x2), atan2(y1, x1), first)

    return min(var1, var2)


print(moscow(xA, yA, xB, yB))
# print(moscow(0, 5, 4, 3))  # 4.636476090008
# print(moscow(0, 5, 4, -3))  # 10.0
