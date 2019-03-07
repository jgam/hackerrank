#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    #initial num we can add later
    #two cases: first get all the same strings
    #second case-> starting from 3 to odd numbers to check if the numbers are palindrome
    
    char_dict =[]
    prev_char = ''
    char_count = 0
    #first case
    ret = 0
    for character in s:
        if character == prev_char:
            char_count += 1
            continue
        else:
            if char_count == 0:
                prev_char = character
                char_count = 1
            else:
                char_dict.append((prev_char, char_count))
                prev_char = character
                char_count = 1
    char_dict.append((prev_char, char_count))

    for index in range(len(char_dict)):
        ret += char_dict[index][1]/2*(char_dict[index][1]+1)
        try:
            different_char = char_dict[index+1][0]
            different_count = char_dict[index+1][1]
            same_char = char_dict[index+2][0]
            same_count = char_dict[index+2][1]
            if char_dict[index][0] != different_char and char_dict[index][0] == same_char:
                if different_count == 1:
                    ret += min(char_dict[index][1], char_dict[index+2][1])
        except:
            continue

    
    #now second case when there is a middle number.
    return int(ret)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
'''
1. Build a list of tuples such that the string "aaabbc" can be squashed down to [("a", 3), ("b", 2), ("c", 1)]. 2. add to answer all combinations of substrings from these tuples which would represent palindromes which have all same letters. 3. traverse this list to specifically find the second case mentioned in probelm
'''