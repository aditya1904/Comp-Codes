#!/bin/python3

# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    drop_c = 0
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabets:
        a_c = a.count(letter)
        b_c = b.count(letter)
        if a_c != b_c:
            drop_c += abs(a_c - b_c)
    return drop_c

if __name__ == '__main__':
    a = input()
    b = input()
    res = makeAnagram(a, b)
    print(res)