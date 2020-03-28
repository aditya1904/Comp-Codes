#!/bin/python3

######################################################################
#  https://www.hackerrank.com/challenges/mark-and-toys/problem       #
######################################################################

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    sum, count = 0, 0
    for price in prices:
        if (sum + price) < k:
            count += 1
            sum += price
            print(sum, count)
        else:
            return count

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))
    print(prices)
    result = maximumToys(prices, k)

    print(result)
