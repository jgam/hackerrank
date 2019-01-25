#this
def minimumBribes(queue):
    lastIndex = len(queue) - 1
    swaps = 0
    swaped = False
    
    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        #finding chaotic here with index pointer moving 2 ahead
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sort
    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            #comps += 1
            if queue[j] > queue[j+1]:
                temp = queue[j]
                queue[j] = queue[j+1]
                queue[j+1] = temp
                swaps += 1
                swaped = True
        
        if swaped:
            swaped = False
        else:
            break
    return swaps
