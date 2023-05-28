def solution(r1, r2):
    answer = 0
    
    # 1사 분면 위의 점만 계산 하여 4배
    cnt = 0
    y_min, y_max = r1, r2
    
    for x in range(0, r2):
        # max를 줄여서 범위를 줄인다.
        while r2**2 < y_max**2 + x**2:
            y_max -= 1
        
        # min을 줄여서 범위를 늘린다.
        while y_min-1 and r1**2 <= (y_min-1)**2 + x**2:
            y_min -= 1
        cnt += y_max - y_min + 1
        # print("x, y_max, y_min", x, y_max, y_min)
        
    return cnt*4