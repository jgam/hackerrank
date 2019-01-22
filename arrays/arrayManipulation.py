#!/bin/python3

import math
import os
import random
import re
import sys
import math
import os
import random
import re
import sys
#this is the import you want.

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l = [0]*(n+1)
    for i in queries:
        l[i[0]-1] += i[2]
        l[i[1]] -= i[2]
    maximum = 0
    tsum = 0
    print('l is: ', l)
    for i in l:
        tsum += i
        if tsum > maximum:
            maximum = tsum
    return maximum
    """
    for i in range(len(queries)):
        for i in range(queries[i][0]-1, queries[i][1]):
            l[i] += queries[i][2]

    return max(l)
    """
#the array needs to be added with the range
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    print('this is n: ', n)
    print('this is m: ', m)
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    print('queries : ', queries)
    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
