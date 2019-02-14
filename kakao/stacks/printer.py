def solution(priorities, location):
    answer = 0
    #a.sort(key=itemgetter(0), reverse=True)
    comp_list = []
    location_num = 1
    for i in range(len(priorities)):
        comp_list.append([priorities[i],i])
    print(comp_list)
    for i in range(len(priorities)):
        if comp_list[i][0] == max(priorities):
            if location == location_num:
                
            comp_list.pop(i)
            location_num += 1
    return answer