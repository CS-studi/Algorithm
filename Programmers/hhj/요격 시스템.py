def solution(targets):
    answer = 0
    missile = -1
    targets.sort(key=lambda x: (x[1], x[0]))
    for s, e in targets:
        if missile <= s or missile > e:
            missile = e
            answer += 1
    return answer