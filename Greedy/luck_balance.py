#!/bin/python3

#https://www.hackerrank.com/challenges/luck-balance/problem

import math
import os
import random
import re
import sys

def key_condition(x):
    return x[0]

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests = sorted(contests, key= lambda x: x[0], reverse=True)
    luck = 0
    for contest in contests:
        if contest[1] == 0:
            luck += contest[0]
        elif contest[1] == 1 and k > 0:
            luck += contest[0]
            k -= 1
        else:
            luck -= contest[0]
    return luck

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)