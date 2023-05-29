from collections import deque
from copy import deepcopy
from itertools import combinations


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def find_safe_space(pnew_walls, pvirus, pboard):
    nboard = deepcopy(pboard)
    # 새 벽을 세운다
    for nx, ny in pnew_walls:
        nboard[nx][ny] = 1

    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque(pvirus)
    while q:
        for _ in range(len(q)):
            vx, vy = q.popleft()
            for k in range(4):
                xx = vx + dx[k]
                yy = vy + dy[k]
                if 0 <= xx < n and 0 <= yy < m:
                    if nboard[xx][yy] == 0 and visited[xx][yy] == 0:
                        visited[xx][yy] = 1
                        nboard[xx][yy] = 2
                        q.append([xx, yy])

    return sum(nboard, []).count(0)


n, m = map(int, input().split())
virus = []
empty = []
board = []
for x in range(n):
    board.append(list(map(int, input().split())))
    for y in range(m):
        if board[x][y] == 2:
            virus.append([x, y])
        elif board[x][y] == 0:
            empty.append([x, y])

answer = -1
case = list(combinations(empty, 3))
for new_walls in case:
    answer = max(answer, find_safe_space(new_walls, virus, board))

print(answer)
