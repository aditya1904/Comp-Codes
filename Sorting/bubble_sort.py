#!/bin/python3

######################################################################
#  https://www.hackerrank.com/challenges/ctci-bubble-sort/problem    #
######################################################################

# Complete the countSwaps function below.
def countSwaps(a):
    min_swaps = 0
    len_of_a = len(a)
    for i in range(0, len_of_a):
        for j in range(0, len_of_a - 1):
            if a[j] > a[j + 1]:
                min_swaps+=1
                a[j+1], a[j] = a[j], a[j+1]
    print("Array is sorted in" , min_swaps , "swaps.")
    print("First Element:" , a[0])
    print("Last Element:" , a[len_of_a - 1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)