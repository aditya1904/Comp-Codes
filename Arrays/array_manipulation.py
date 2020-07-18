#!/bin/python3

##############################################################
# https://www.hackerrank.com/challenges/crush/problem        #
##############################################################

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    init_dict = [0]*n #{i:0 for i in range(1, n+1)}
    max_val, q_sum=0,0
    for query in queries:
        init_dict[query[0]-1] += query[2]
        if query[1] < n:
            init_dict[query[1]] -= query[2]
    for i in range(0, n):
        q_sum += init_dict[i]
        if q_sum > max_val:
            max_val = q_sum
    return max_val

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
