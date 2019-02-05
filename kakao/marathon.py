import time

def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
    return participant[0]
    
    #this taking too much time
    '''
    participant = sorted(participant)
    completion = sorted(completion)
    for i in range(len(participant)-1):
        if participant[i] == completion[i]:
            continue
        else:
            return participant[i]
    return participant[-1]
    '''
participant = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']

t1 = time.time()
print(solution(participant, completion))
t2 = time.time()
print(t2-t1)

#better records
'''
6.604194641113281e-05
7.390975952148438e-05
7.009506225585938e-05
6.008148193359375e-05
'''

#original records
'''
'''