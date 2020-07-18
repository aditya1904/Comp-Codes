#!/bin/python3

# https://www.hackerrank.com/challenges/frequency-queries/problem

# Complete the freqQuery function below.
def freqQuery(queries):
    ht, freq = {}, {}
    answers = []
    for query in queries:
        if(query[0] == 1):
            if not ht.__contains__(query[1]):
                ht[query[1]] = 1
                freq[ht[query[1]]] = freq[ht[query[1]]] + 1 if freq.__contains__(ht[query[1]]) else 1
            else:
                freq[ht[query[1]]] -= 1
                ht[query[1]] += 1
                freq[ht[query[1]]] = freq[ht[query[1]]] + 1 if freq.__contains__(ht[query[1]]) else 1
        elif (query[0] == 2):
            if ht.__contains__(query[1]) and ht[query[1]] != 0:
                freq[ht[query[1]]] = freq[ht[query[1]]] - 1
                ht[query[1]] = ht[query[1]] - 1
                freq[ht[query[1]]] = freq[ht[query[1]]] + 1 if freq.__contains__(ht[query[1]]) else 1
        elif (query[0] == 3):
            answers.append(1) if freq.__contains__(query[1]) and freq[query[1]] > 0 else answers.append(0)
    return answers

if __name__ == '__main__':
    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)


# This function could not execute in time for one case
# def freqQuery(queries):
#     ht = {}
#     freq = {}
#     answers = []
#     for query in queries:
#         if(query[0] == 1):
#             ht[query[1]] = 1 if not ht.__contains__(query[1]) else ht[query[1]] + 1
#         elif (query[0] == 2):
#             if ht.__contains__(query[1]) and ht[query[1]] != 0:
#                 ht[query[1]]= ht[query[1]] - 1
#         elif (query[0] == 3):
#             answers.append(1) if ht.values().__contains__(ht[query[1]]) else answers.append(0)
#     return answers
