#!/bin/python3

# https://www.hackerrank.com/challenges/count-triplets-1/problem

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    number_di={}
    triplets=0
    for pos, number in enumerate(arr):
        if number_di.__contains__(number):
            number_di[number].append(pos)
        else:
            number_di[number]=[pos]
        print(number_di)
    print(number_di)
    return triplets

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)