#!/bin/python3

# https://www.hackerrank.com/challenges/alternating-characters/problem

def next_char(char):
    if char == 'A':
        return 'B'
    return 'A'


# Complete the makeAnagram function below.
def alt_chars(a):
    count = 0
    current_char = a[0]
    reqd_next = next_char(current_char)
    for i in range(1, len(a)):
        if a[i] != reqd_next:
            count += 1
        else:
            current_char = a[i]
            reqd_next = next_char(current_char)
    return count


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        a = input()
        print(alt_chars(a))
