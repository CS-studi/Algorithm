from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
d_map = {
    (0, -1): {"D": 3, "L": 2},
    (0, 1): {"D": 2, "L": 3},
    (-1, 0): {"D": 0, "L": 1},
    (1, 0): {"D": 1, "L": 0}
}


def bfs():
    q = deque([[deque([(0, 0)]), 0, 0]])
    while q:
        snake, sdirect, count = q.popleft()

        sx, sy = snake[0]
        sx += dx[sdirect]
        sy += dy[sdirect]
        count += 1

        # check
        if (sx, sy) in snake:  # 몸에 부딪힌 경우
            return count
        if not (0 <= sx < n and 0 <= sy < n):  # 벽에 부딪힌 경우
            return count

        snake.appendleft((sx, sy))  # 머리를 다음 칸에

        # find apple
        if (sx + 1, sy + 1) in apples:
            apples.remove((sx + 1, sy + 1))
        else:  # 꼬리 빼기
            snake.pop()

        # change direction
        if count in directions:
            sdirect = d_map[(dx[sdirect], dy[sdirect])][directions[count]]

        q.append([snake, sdirect, count])
    return 1


n = int(input())
apples = {tuple(map(int, input().split())) for _ in range(int(input()))}
directions = {}
for _ in range(int(input())):
    lcount, ldirect = list(input().split())
    directions[int(lcount)] = ldirect

print(bfs())