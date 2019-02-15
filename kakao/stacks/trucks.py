def solution(bridge_length, weight, truck_weights):
    answer = 0
    index = 0
    progress = []
    for Tweight in truck_weights:
        print('real', progress)
        if len(progress) <= bridge_length:
            print('sum should be 0 :', sum(progress))
            if (sum(progress)+Tweight) <= weight:
                progress.append(Tweight)
                answer += 1
                print('progres should be 7 : ', progress,answer)
            else:
                current_sum = sum(progress)
                while sum(progress)+Tweight >= weight:
                    print('first else niqqa!!')
                    progress.pop(0)
                    popped_time = bridge_length - len(progress)
                    answer += popped_time
                progress.append(Tweight)
                print(answer)
        else:
            current_sum = sum(progress)
            while sum(progress)+Tweight >= weight:
                print('2nd else niqqa!!')
                progress.pop(0)
                popped_time = bridge_length - len(progress)
                answer += popped_time
            progress.append(Tweight)
            print(answer)
            
    return answer+bridge_length
print(solution(2,10,[7,4,5,6]))