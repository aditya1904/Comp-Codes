#!/bin/python3

#####################################################################
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem     #
#####################################################################

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    minSwaps = 0
    sortedArray = sorted(arr)
    for i in range(len(sortedArray) - 1):
        number = i + 1
        wantedPosition = i
        currentPosition = arr.index(number)
        if ( wantedPosition != currentPosition):
            arr[currentPosition], arr[wantedPosition] = arr[wantedPosition], arr[currentPosition]
            minSwaps += 1
    return minSwaps


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)
