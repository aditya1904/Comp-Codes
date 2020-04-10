#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

# Complete the makeAnagram function below.
def valid_string(a):
    count_alphabets = {}
    count_counts = {0:0, 1: 0}
    alp = "abcdefghijklmnopqrstuvwxyz"
    for letter in alp:
         count_alphabets[letter] = 0
    for l in a:
        count_counts[count_alphabets[l]] -= 1
        count_alphabets[l] += 1
        if count_alphabets[l] not in count_counts.keys():
            count_counts[count_alphabets[l]] = 1
        else:
            count_counts[count_alphabets[l]] += 1
    count_counts = {k:v for k,v in count_counts.items() if v > 0}
    leng = len(count_counts.keys())
    if leng == 1:
        return "YES"
    elif leng > 2:
        return "NO"
    else:
        if count_counts.__contains__(1) and count_counts[1] == 1:
            return "YES"
        else:
            l = list(count_counts.keys())
            l.sort()
            min = l[0]
            if count_counts.__contains__(min + 1) and count_counts[min+1] == 1:
                return "YES"
            else:
                return "NO"

if __name__ == '__main__':
    a = input()
    res = valid_string(a)
    print(res)