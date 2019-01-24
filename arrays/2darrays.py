def hourglassSum(arr):
    sum_num = 0
    first_cond = True
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            current_sum_num = sum(arr[i][j:j+3])+sum(arr[i+2][j:j+3])+arr[i+1][j+1]
            if first_cond:
                sum_num = current_sum_num
                first_cond = False
            if current_sum_num > sum_num:
                sum_num = current_sum_num
    return sum_num