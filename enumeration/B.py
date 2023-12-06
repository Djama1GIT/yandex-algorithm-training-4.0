def aviary(matrix, column, n):
    if column >= n:
        return 1
    count = 0
    for i in range(n):
        if check(matrix, i, column, n):
            matrix[i][column] = True
            count += aviary(matrix, column + 1, n)
            matrix[i][column] = False
    return count


def check(matrix, row, column, n):
    for i in range(column):
        if matrix[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if matrix[i][j]:
            return False
    for i, j in zip(range(row, n, 1), range(column, -1, -1)):
        if matrix[i][j]:
            return False
    return True


N = int(input())
placement = [[False] * N for _ in range(N)]
print(aviary(placement, 0, N))
