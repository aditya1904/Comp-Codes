#!/bin/python3

########################################################################
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem  #
########################################################################

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    position, jumps = 0, 0
    length = len(c)
    while position < length - 1:
        if position == length - 2:
            position += 2
        else:
            if c[position + 2] == 0:
                position += 2
            else:
                position += 1
        jumps += 1
    return jumps

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)