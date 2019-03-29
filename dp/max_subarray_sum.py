#given an array of unordered positive and negative integers, find the maxiuum subarray sum in the array

array = [2, -9, 5, 1, -4, 6, 0, -7, 8]

def kadaneAlgo(input):
    maxSum = 0
    curSum = 0
    for i in input:
        curSum += i
        if curSum > maxSum:
            maxSum = curSum
        
        if curSum < 0:
            curSum = 0
    return maxSum

print(kadaneAlgo(array))