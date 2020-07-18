#!/bin/python3

# common-child LCS

def common_child(n1, n2, size):
    L = [[0]*(size+1) for j in range(size+1)]
    for i in range(size+1):
        for j in range(size+1):
            if i==0 or j==0:
                L[i][j] = 0
            elif n1[i-1] == n2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    return L[size][size]


if __name__ == '__main__':
    n1 = input()
    n2 = input()
    result = common_child(n1, n2, len(n1))
    print(result)
