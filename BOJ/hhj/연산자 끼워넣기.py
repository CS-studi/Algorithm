def dfs(i, value, add, minus, multiply, divide):
    if add + minus + multiply + divide == 0:
        data.append(value)
        return
    if i >= len(arr):
        return

    if add:
        dfs(i + 1, value + arr[i + 1], add - 1, minus, multiply, divide)
    if minus:
        dfs(i + 1, value - arr[i + 1], add, minus - 1, multiply, divide)
    if multiply:
        dfs(i + 1, value * arr[i + 1], add, minus, multiply - 1, divide)
    if divide:
        d_val = value // arr[i + 1] if value >= 0 else -(abs(value) // arr[i + 1])
        dfs(i + 1, d_val, add, minus, multiply, divide - 1)


n = int(input())
arr = list(map(int, input().split()))
operations = tuple(map(int, input().split()))
data = []
dfs(0, arr[0], operations[0], operations[1], operations[2], operations[3])
print(max(data))
print(min(data))
