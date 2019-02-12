from random import sample
from functools import reduce
from operator import mul


def solution(clothes):
    answer = 0
    clothes_dict = {}
    single_count = 0
    for clothing in clothes:
        if clothing[1] in clothes_dict:
            clothes_dict[clothing[1]] += 1
        else:
            clothes_dict[clothing[1]] = 1
    #so far is the dictionary parsing
    actual_list = [i+1 for i in clothes_dict.values()]
    ret = reduce(mul, actual_list)
    return ret-1