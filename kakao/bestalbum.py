from operator import itemgetter
def solution(genres, plays):
    answer = []
    hash_dict = {}
    ret_list = []
    #unsorted_list.sort(key=lambda x: x[3])
    for i in range(len(genres)):
        if genres[i] in hash_dict:
            hash_dict[genres[i]][0] += plays[i]
            hash_dict[genres[i]].append([plays[i],i])
            print(9)
        else:
            added_list = [plays[i]]
            added_list.append([plays[i],i])
            hash_dict[genres[i]] = added_list
            
    a = list(hash_dict.values())
    a.sort(key=itemgetter(0), reverse=True)
    ret_list = []
    for i in a:
        i.pop(0)
        i.sort(key=itemgetter(0), reverse=True)
        while_counter = 0
        if len(i) == 1:
            ret_list.append(i[0][1])
        else:
            while while_counter < 2:
                ret_list.append(i[while_counter][1])
                while_counter += 1
    #hash_dict => 'classic':(1450,(1,500),(2))
    return ret_list