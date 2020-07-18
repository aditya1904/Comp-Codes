#!/bin/python3

############################################################################
# https://www.hackerrank.com/challenges/2d-array/problem                   #
############################################################################

import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max = -sys.maxsize
    for i in range(4):
        for j in range(4):
            tempsum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if tempsum > max : max = tempsum
    return max

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
