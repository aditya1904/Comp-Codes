#!/bin/python3

# https://www.hackerrank.com/challenges/special-palindrome-again/problem

def substrCount(n, s):
    count = 0
    for i in range(n):
        count += 1
        if i + 1 < n and s[i] == s[i + 1]:
            j = i + 1
            while j < n and s[i] == s[j]:
                count += 1
                j += 1
        elif i - 1 >= 0 and i + 1 < n and s[i - 1] == s[i + 1]:
            char = s[i - 1]
            j, k = i - 1, i + 1
            while j >= 0 and k < n and s[j] == s[k] == char:
                count += 1
                j -= 1
                k += 1
    return count


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)
