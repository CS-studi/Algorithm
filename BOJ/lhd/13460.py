import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
red = []
blue = []


# 구슬 옮기는 함수
def move_marble(x, y, dx, dy):
    # 옮긴 위치 반환, 움직인 칸 수
    move = 0
    while graph[x+dx][y+dy] != '#':
        # 구멍으로 탈출할 경우 0,0 return
        if graph[x+dx][y+dy] == 'O':
            return 0, 0, 0
        x += dx
        y += dy
        move += 1
    
    return x, y, move


# 구슬을 이동한 뒤 발생하는 bfs
def bfs():
    visited = {}
    q = deque([])
    q.append(red+blue)
    
    visited[red[0], red[1], blue[0], blue[1]] = 0
    while q:
        rx, ry, bx, by = q.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            rnx, rny, rmove = move_marble(rx, ry, dx, dy)
            bnx, bny, bmove = move_marble(bx, by, dx, dy)
            if not bnx and not bny:
                continue
            elif not rnx and not rny:
                print(visited[rx, ry, bx, by] + 1)
                return
            elif rnx == bnx and rny == bny:
                if rmove > bmove:
                    rnx -= dx
                    rny -= dy
                else:
                    bnx -= dx
                    bny -= dy
            if (rnx, rny, bnx, bny) not in visited:
                visited[rnx, rny, bnx, bny] = visited[rx, ry, bx, by] + 1
                q.append([rnx, rny, bnx, bny])

        if not q or visited[rx, ry, bx, by] >= 10:
            print(-1)
            return

for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            graph[i][j] = '.'
            red = [i, j]
        elif graph[i][j] == 'B':
            graph[i][j] = '.'
            blue = [i, j]

bfs()
