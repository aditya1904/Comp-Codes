#!/bin/python3

import math

def nCr(n):
    f = math.factorial
    if n > 1:
        return f(n) / 2 / f(n-2)
    else:
        return 0

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    anagram_dict = {}
    for i in range(len(s)):
        j, end = 0, i + 1
        while end < len(s) + 1:
            word = ''.join(sorted(s[j:end]))
            anagram_dict[word] = 1 if not anagram_dict.__contains__(word) else anagram_dict[word] + 1
            j += 1
            end += 1
    print(anagram_dict)
    return int(sum(list(map(nCr, anagram_dict.values()))))

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
