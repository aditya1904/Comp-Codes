#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if s1.find(char) > -1 and s2.find(char) > -1:
            return "YES"
    return "NO"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)
