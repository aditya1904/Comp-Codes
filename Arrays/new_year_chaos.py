#!/bin/python3

##################################################################
# https://www.hackerrank.com/challenges/new-year-chaos/problem   #
##################################################################

def minimumBribes(q):
    min_bribes = 0
    for pos, item in enumerate(q):
        if (item - 1) - pos > 2:
            print("Too chaotic")
            return
        for i in range(max(0,item-2), pos):
            if q[i] > item:
                min_bribes+=1
    print(min_bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
