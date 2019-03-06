#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(character):
    #keep the values with max in dict
    sherlock = {}
    max_num = 0
    no_cond = False
    word_count = 0
    same_count = 0
    if len(character) == 1:
        return "YES"
    for s in character:
        word_count += 1
        if s in sherlock:
            sherlock[s] += 1
            if sherlock[s] > max_num:
                max_num = sherlock[s]
                same_count = 1
            elif sherlock[s] == max_num:
                no_cond = True
                same_count += 1
        else:
            sherlock[s] = 1
    
    max_count = 0
    no_condi = False
    print(sherlock)
    for value in sherlock.values():
        if max_num - value == 1:
            if no_condi:
                return "NO"
            max_count += 1
            print('this should be printed twice', len(sherlock))

        elif max_num - value == 0:
            continue
        else:
            if value == 1:
                if no_condi:
                    return "NO"
                no_condi = True
                continue
            return "NO"
    #now we have dict and max_num
    if max_count > 1 and max_count != len(sherlock)-1:
        return "NO"

    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
