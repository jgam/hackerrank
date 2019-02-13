def solution(arrangement):
    answer = 0
    #string manipulation
    #use stacks and queue as well
    last = ''
    num_count = 0
    for i in arrangement:
        if i == '(':
            last = 'open'
            num_count += 1
            continue
        else:
            if last == 'open':
                num_count -= 1
                answer += num_count
                last = 'close'
            else:
                num_count -= 1
                answer += 1
    return answer
