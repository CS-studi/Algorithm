from collections import deque
from copy import deepcopy

# {0: "상", 1: "하", 2: "좌", 3: "우"}
def get_board(direction, dboard):
    tboard = deepcopy(dboard)
    if direction < 2:  # 상하
        tboard = list(map(list, zip(*tboard)))

    if direction % 2 == 0:  # 왼쪽 부터
        for i in range(n):
            temp = deque([])
            is_added = False
            q = deque(tboard[i])
            while q:
                now = q.popleft()
                if now == 0:
                    continue

                if not temp:
                    temp.append(now)
                elif temp[-1] != now:
                    temp.append(now)
                    is_added = False
                elif temp[-1] == now:
                    if is_added:
                        temp.append(now)
                        is_added = False
                    else:
                        temp[-1] += now
                        is_added = True
            z_list = [0 for _ in range(n - len(temp))]
            tboard[i] = list(temp) + z_list
    else:  # 오른쪽 부터
        for i in range(n):
            temp = deque([])
            is_added = False
            q = deque(tboard[i])
            while q:
                now = q.pop()
                if now == 0:
                    continue

                if not temp:
                    temp.appendleft(now)
                elif temp[0] != now:
                    temp.appendleft(now)
                    is_added = False
                elif temp[0] == now:
                    if is_added:
                        temp.appendleft(now)
                        is_added = False
                    else:
                        temp[0] += now
                        is_added = True
            z_list = [0 for _ in range(n - len(temp))]
            tboard[i] = z_list + list(temp)

    if direction < 2:  # 상하
        tboard = list(map(list, zip(*tboard)))

    return tboard


def dfs(count, dboard):
    if count == 5:
        return max(e for arr in dboard for e in arr)

    result = -1
    for d in range(4):
        result = max(result, dfs(count + 1, get_board(d, dboard)))

    return result


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, board))