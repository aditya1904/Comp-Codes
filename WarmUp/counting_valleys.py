#!/bin/python3

########################################################################
# https://www.hackerrank.com/challenges/counting-valleys/problem       #
########################################################################

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level, current_level, valley_count = 0, 0, 0
    in_valley = False
    for step in s:
        if current_level < sea_level  and in_valley == False:
            valley_count += 1
            in_valley = True
        if current_level == sea_level:
            in_valley = False
        if step == 'U':
            current_level += 1
        if step == 'D':
            current_level += -1
    return valley_count

if __name__ == '__main__':
    n = int(input())
    s = raw_input()
    result = countingValleys(n, s)
    print result

