import math

def solution(r1, r2):
    q_count = 0
    s_r1 = r1 ** 2
    s_r2 = r2 ** 2
    
    for x in range(1, r2 + 1):
        temp = s_r1 - x ** 2
        min_y = math.ceil(math.sqrt(temp)) if temp > 0 else 0
        max_y = math.floor(math.sqrt(s_r2 - x ** 2))
        q_count += max_y - min_y + 1
    return 4 * q_count