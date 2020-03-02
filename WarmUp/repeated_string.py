#!/bin/python3

########################################################################
# https://www.hackerrank.com/challenges/repeated-string/problem        #
########################################################################

def cal_no_of_a(s):
   return s.count('a')

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_of_s = len(s)
    x = cal_no_of_a(s)
    xs = int(n/len_of_s) * x
    y = n%len_of_s
    return xs + cal_no_of_a(s[:y])

if __name__ == '__main__':
    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
