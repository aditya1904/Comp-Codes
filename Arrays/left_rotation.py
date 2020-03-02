#!/bin/python3

############################################################################
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem   #
############################################################################

# Complete the rotLeft function below.
def rotLeft(a, d):
    length = len(a)
    ret_arr = [0] * length
    for index, item in enumerate(a):
        ret_arr[(index - d)%length] = item
    return ret_arr

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
    print(result)