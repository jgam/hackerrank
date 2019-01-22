#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #minswap is done by using the graphs & nodes
    #simply get each number of swaps for cycles and sum of those numbers subtracted by 1.
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda x:x[1])
    #up until here sorted the array by its values and positions are shown

    #tracking of visitied elements, initializing all elements as not visited as false
    vis = {k:False for k in range(n)}
    ans = 0
    #arrpos => [(2, 1), (3, 2), (1, 3), (0, 4)]
    #vis => {0: False, 1: False, 2: False, 3: False}
    #n => 4
    for i in range(n):
        #already swapped or present at correct position
        if vis[i] or arrpos[i][0] == i:
            continue
        
        #here we find the number of nodes in the cycle and add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            #make node as visited
            vis[j] = True
            #move to the next node
            j = arrpos[j][0]
            cycle_size += 1
        #update answer by adding current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
