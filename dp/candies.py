def candies(n, arr):
    cmp_list = [1] * n
    local_min = 0
    total_candy = 0
    #compare the increasing order only
    #find the local minima and subtract
    for index in range(1,n):
        if arr[index] > arr[index-1]:
            cmp_list[index] = cmp_list[index-1] + 1
    print(cmp_list)
    
    for index in range(n-2, -1, -1):
        if arr[index] > arr[index+1]:
            if cmp_list[index] > cmp_list[index+1]:
                continue
            else:
                cmp_list[index] = cmp_list[index+1] + 1
    print(cmp_list)
    return sum(cmp_list)

#this was not specifically dynamic
# the two tricks
#1. start everything with 1 and current is previous + 1
#finding local minima and don't add previous + 1 to that minima
#thats it
