import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n)]

# 사과 정보 입력 받기
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

# 방향 변환 횟수
turns = deque([])
l = int(input())
for _ in range(l):
    a, b = input().rsplit()
    turns.append([int(a), b])

# 초기 방향



def bfs(x, y):
    q = deque([])
    q.append([x, y, 0, 0])
    dx = [0, -1, 0, 1] # 오른쪽, 위, 왼쪽, 아래
    dy = [1, 0, -1, 0] # 'D' 는 방향 감소, 'L' 방향 증가
    toward = 0
    snake = deque([])
    snake.append([x, y])

    while q:
        x, y, time, tow = q.popleft()
        if turns:
            t, d = turns.popleft()
            if time == t:
                if d == 'D':
                    toward -= 1
                    toward %= 4
                elif d == 'L':
                    toward += 1
                    toward %= 4
            else:
                turns.appendleft([t, d])
        
        rx, ry = x + dx[toward], y + dy[toward]
        if 0 > rx or rx >= n or ry < 0 or ry >= n or [rx, ry] in snake:
            return time+1
        if 0 <= rx < n and 0 <= ry < n:
            if graph[rx][ry] == 1: # 사과
                graph[rx][ry] = 0
                snake.append([rx, ry])
                q.append([rx, ry, time+1, tow])
            elif graph[rx][ry] == 0:
                q.append([rx, ry, time+1, tow])
                snake.append([rx, ry])
                snake.popleft()


print(bfs(0, 0))
