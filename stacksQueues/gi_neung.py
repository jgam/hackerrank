import math
def solution(progresses, speeds):
    answer = []
    print(progresses)
    print(speeds)
    for i in range(len(progresses)):
        to_do = 100 - progresses[i]
        days_left = math.ceil(to_do / speeds[i])
        answer.append(days_left)
    
    ret_list = []
    origin_num = answer[0]
    count = 1
    for n_index in range(1, len(answer)):
        if answer[n_index] > origin_num:
            ret_list.append(count)
            #however, later values that are less than the number right beforehand?
            origin_num = answer[n_index]
            count = 1
        else:
            count += 1
            continue
    ret_list.append(count)
            
    return ret_list