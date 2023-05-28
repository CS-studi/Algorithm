import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))
dice = [0 for _ in range(6)]
# 동 1 서 2 북 3 남 4
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# 한번에 네개의 주사위만 돌아감
'''
동 -> bottom -> left, left -> top, top -> right, right -> bottom
'''

#바닥 6에서 시작
# 주사위 윗면(0), 북쪽(1), 동쪽(2), 서쪽(3), 남쪽(4), 바닥(5)
for i in range(k):
    toward = order[i] - 1
    nx = x + direction[toward][0]
    ny = y + direction[toward][1]

    if (not 0 <= nx < n) or (not 0 <= ny < m):
        continue
    # 동
    if toward == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 서
    elif toward == 1:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 북
    elif toward == 2:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    # 남
    elif toward == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[5]
    else:
        dice[5] = graph[nx][ny]
        graph[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[0])