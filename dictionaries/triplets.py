#!/bin/python3

import math
import os
import random
import re
import sys
import csv


# Complete the countTriplets function below.
def countTriplets(arr, r):
    basic_dict = {}
    for i in arr:
        if i in basic_dict:
            basic_dict[i] += 1
        else:
            basic_dict[i] = 1
    ret = 0
    print(basic_dict)
    original_num = len(arr)
    if r == 1:
        #get combinations
        return original_num * (original_num-1) * (original_num-2) // 6
    #here we can set the range
    for_range = int(math.log(max(basic_dict),r))
    #because something**0 is 1, you have to start from 
    if 1 in basic_dict:
        for_range += 1

    for i in range(for_range-2):
        if r**i in basic_dict:
            if r**(i+1) in basic_dict:
                if r**(i+2) in basic_dict:
                    ret += basic_dict[r**i] * basic_dict[r**(i+1)] * basic_dict[r**(i+2)]
                else:
                    continue
            else:
                continue
        else:
            continue

    if len(basic_dict) == 1:
        ret = basic_dict.values()
    return ret
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, r = 1, 1

    with open('input_triplets.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                row = ' '.join(row)
                n = int(row[0])
                r = int(row[1])
                line_count += 1
            else:
                arr = [i for i in row.split(' ')]
                line_count += 1

    print('n and r is ', n, r)

    #nr = input().rstrip().split()

    #n = int(nr[0])

    #r = int(nr[1])

    #arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    #fptr.write(str(ans) + '\n')

    #fptr.close()
