#!/bin/python3

####################################################################
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem   #
####################################################################

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict={}
    for word in magazine:
        mag_dict[word] = 1 if not mag_dict.__contains__(word) else mag_dict[word] + 1
    for word in note:
        if mag_dict.__contains__(word) and mag_dict[word] is not 0:
            mag_dict[word] = mag_dict[word] - 1
        else:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)




