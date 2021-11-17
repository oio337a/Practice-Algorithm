import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
check = [[-1]*n for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    if check[x][y] != -1:
        return check[x][y]
    check[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if board[nx][ny] < board[x][y]:
                check[x][y] += dfs(nx, ny)
    return check[x][y]


print(dfs(0, 0))
