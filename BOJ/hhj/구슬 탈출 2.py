from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(prx, pry, pbx, pby, pvisited):
    q = deque([[prx, pry, pbx, pby, 0, pvisited]])
    while q:
        rx, ry, bx, by, count, rvisited = q.popleft()
        if count >= 10:
            continue

        for k in range(4):
            r_count, b_count = 0, 0  # 두 구슬이 겹칠때 사용

            # move blue
            bxx, byy = bx, by
            while board[bxx][byy] == ".":
                bxx += dx[k]
                byy += dy[k]
                if (bxx, byy) == (hx, hy):
                    break
                if board[bxx][byy] == "#":
                    bxx -= dx[k]
                    byy -= dy[k]
                    break
                b_count += 1

            # move red
            rxx, ryy = rx, ry
            while board[rxx][ryy] == ".":
                rxx += dx[k]
                ryy += dy[k]
                if (rxx, ryy) == (hx, hy):
                    break
                if board[rxx][ryy] == "#":
                    rxx -= dx[k]
                    ryy -= dy[k]
                    break
                r_count += 1

            # move 보정
            if (bxx, byy) == (rxx, ryy):
                if (bxx, byy) == (hx, hy):  # 동시에 빠지면 무효
                    continue
                if r_count < b_count:  # 이동횟수가 적은 구슬이 더 앞에 있음
                    bxx -= dx[k]
                    byy -= dy[k]
                else:
                    rxx -= dx[k]
                    ryy -= dy[k]

            # check
            if (bxx, byy) == (hx, hy):  # 파란공 먼저 빠지면 무효
                continue
            if (rxx, ryy) == (hx, hy):
                return count + 1

            # q append
            if (rxx, ryy, bxx, byy) not in rvisited:
                rvisited.add((rxx, ryy, bxx, byy))
                q.append([rxx, ryy, bxx, byy, count + 1, rvisited])

    return -1


n, m = map(int, input().split())
board = []
marble = []
rx, ry, bx, by = 0, 0, 0, 0
hx, hy = 0, 0
for x in range(n):
    board.append(list(input()))
    for y in range(m):
        if board[x][y] == "R":
            board[x][y] = "."
            rx, ry = x, y
        elif board[x][y] == "B":
            board[x][y] = "."
            bx, by = x, y
        elif board[x][y] == "O":
            board[x][y] = "."
            hx, hy = x, y

print(bfs(rx, ry, bx, by, {(rx, ry, bx, by)}))