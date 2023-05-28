import sys
import copy

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def checkSame(board, n):
    maxV = -1
    ttmp = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                maxV = max(board[i][j], maxV)
                ttmp.append(board[i][j])

    if len(ttmp) != len(set(ttmp)):
        return True, maxV
    else:
        return False, maxV
            

def move_block(board, d):
    tmp = copy.deepcopy(board)
    visited = [False]*n
    
    if d == 1: # 위
        for j in range(n):  
            visited = [False]*n
            for i in range(1, n):
                if tmp[i][j] != 0:
                    row = i
                    while row > 0 and tmp[row-1][j] == 0:
                        row -= 1
                    if row > 0 and tmp[row-1][j] == tmp[i][j] and not visited[row-1]:
                        tmp[row-1][j] *= 2
                        tmp[i][j] = 0
                        visited[row-1] = True
                    else:
                        tmp[row][j], tmp[i][j] = tmp[i][j], tmp[row][j]
            
    elif d == 2: # 아래
        for j in range(n):
            visited = [False]*n
            for i in range(n-2, -1, -1):
                if tmp[i][j] != 0:
                    row = i
                    while row < n-1 and tmp[row+1][j] == 0:
                        row += 1
                    if row < n-1 and tmp[row+1][j] == tmp[i][j] and not visited[row+1]:
                        tmp[row+1][j] *= 2
                        tmp[i][j] = 0
                        visited[row+1] = True
                    else:
                        tmp[row][j], tmp[i][j] = tmp[i][j], tmp[row][j]
    elif d == 3: # 오른쪽
        for i in range(n):
            visited = [False]*n
            for j in range(n-2, -1, -1):
                if tmp[i][j] != 0:
                    col = j
                    while col < n-1 and tmp[i][col+1] == 0:
                        col += 1
                    
                    if col < n-1 and tmp[i][col+1] == tmp[i][j] and not visited[col+1]:
                        tmp[i][col+1] *= 2
                        tmp[i][j] = 0
                        visited[col+1] = True
                    else:
                        tmp[i][col], tmp[i][j] = tmp[i][j], tmp[i][col]

    elif d == 4: # 왼쪽
        for i in range(n):
            visited = [False]*n
            for j in range(1, n):
                if tmp[i][j] != 0:
                    col = j
                    while col > 0 and tmp[i][col-1] == 0:
                        col -= 1
                    if col >0 and tmp[i][col-1] == tmp[i][j] and not visited[col-1]:
                        tmp[i][col-1] *= 2
                        tmp[i][j] = 0
                        visited[col-1] = True
                    else:
                        tmp[i][col], tmp[i][j] = tmp[i][j], tmp[i][col]

    return tmp
ans = 0
# board = move_block(board, 3)

def dfs(board, n, depth):
    global ans
    flag, maxV = checkSame(board, n)
    if depth == 5:
        ans = max(ans, maxV)
        # for i in range(n):
        #     print(*board[i])
        return
    if not flag:
        ans = max(maxV, ans)
        return
    
    ttmp = copy.deepcopy(board)
    for i in range(4):
        ttmp = move_block(ttmp, i+1)
        dfs(ttmp, n, depth+1)
        ttmp = copy.deepcopy(board)


dfs(board, n, 0)

print(ans)