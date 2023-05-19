def solution(targets):
    answer = 0
    targets.sort(key=lambda x : (x[-1], x[0]))
    s, e = 0, 0
    
    '''
    x축으로만 어디서부터 어디까지 인지 계산하여 나타낸다.
    x를 이동시키면서 최소한으로 폭격을 가하여 미사일을 격추 시키는지 계산해야함.
    '''
    
    for target in targets:
        if target[0] >= e:
            print(target)
            answer += 1
            e = target[1]
            
    return answer