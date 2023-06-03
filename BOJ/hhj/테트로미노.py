def get_max1():
    # 1 x 4
    data = set()
    for x in range(n):
        for y in range(m - 4 + 1):
            data.add(sum(board[x][y:y + 4]))

    t_board = list(map(list, zip(*board)))  # transpose
    
    for x in range(m):
        for y in range(n - 4 + 1):
            data.add(sum(t_board[x][y:y + 4]))

    return max(data)


def get_max2():
    # 2 x 2
    data = set()
    for x in range(n - 2 + 1):
        for y in range(m - 2 + 1):
            data.add(sum(board[x][y:y + 2]) + sum(board[x + 1][y:y + 2]))

    return max(data)


def get_max345(r_board):
    # 3 x 2
    data = set()
    shapes = [
        # L (회전, 대칭)
        [(0, 0), (1, 0), (2, 0), (2, 1)],
        [(0, 1), (1, 1), (2, 0), (2, 1)],
        [(0, 0), (0, 1), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (1, 1), (2, 1)],
        # 번개 모양
        [(0, 0), (1, 0), (1, 1), (2, 1)],
        [(0, 1), (1, 0), (1, 1), (2, 0)],
        # ㅜ
        [(0, 0), (1, 0), (1, 1), (2, 0)],
        [(0, 1), (1, 0), (1, 1), (2, 1)],
    ]

    for _ in range(2):
        # 0, 180
        for x in range(n - 3 + 1):
            for y in range(m - 2 + 1):
                for shape in shapes:
                    data.add(sum([r_board[x + sx][y + sy] for sx, sy in shape]))

        # 회전
        r_board = list(map(list, zip(*r_board[::-1])))

        # 90, 270
        for x in range(m - 3 + 1):
            for y in range(n - 2 + 1):
                for shape in shapes:
                    data.add(sum([r_board[x + sx][y + sy] for sx, sy in shape]))
        # 회전
        r_board = list(map(list, zip(*r_board[::-1])))

    return max(data)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(max(get_max1(), get_max2(), get_max345(board)))
