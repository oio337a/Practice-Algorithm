# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

move_cnt = 1
break_cnt = 0

def bfs(x, y):
    global move_cnt, break_cnt
    q = deque()
    q.append([x, y])
    visit = [[0] * m for i in range(n)]
    visit[x][y] = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0 <= x < n and 0 <= y < m and visit[x][y] == 0:
                if board[x][y] == 1 and break_cnt == 0:
                    break_cnt = 1
                    visit[x][y] = 1
                elif board[x][y] == 1 and break_cnt == 1:
                    continue
                visit[x][y] = 1
                q.append([x, y])
                move_cnt += 1
bfs(0, 0)
print(move_cnt)