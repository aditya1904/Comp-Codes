#!/bin/python3

########################################################################
# https://www.hackerrank.com/challenges/sock-merchant/problem          #
########################################################################

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    numbers = {}
    for number in ar:
        if number not in numbers:
            numbers[number] = 1
        else:
            numbers[number] += 1

    return sum(list(map(lambda x: int(x / 2), numbers.values())))


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, raw_input().rstrip().split()))

    result = sockMerchant(n, ar)
    print result