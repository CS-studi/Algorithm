direct_map = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}


def clean():
    def check(cx, cy):
        return 0 <= cx < n and 0 <= cy < m

    def dfs(x, y, direction, count):
        # 청소
        if visited[x][y] == 0:
            visited[x][y] = count

        temp_d = direction
        for _ in range(4):
            temp_d = 3 if temp_d == 0 else temp_d - 1
            dx, dy = direct_map[temp_d]
            xx = x + dx
            yy = y + dy
            # 청소 안 한 곳
            if check(xx, yy) and visited[xx][yy] == 0 and board[xx][yy] == 0:
                return dfs(xx, yy, temp_d, count + 1)

        dx, dy = direct_map[direction]
        xx = x - dx
        yy = y - dy

        if check(xx, yy) and board[xx][yy] == 0:
            return dfs(xx, yy, direction, count)

    dfs(r, c, d, 1)
    return max(sum(visited, []))


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
print(clean())
