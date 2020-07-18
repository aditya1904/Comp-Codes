from typing import *
def toposort(graph, index, temporary_visited, permanent_visited, result, cycle):
    if permanent_visited[index]:
        return result
    if temporary_visited[index]:
        cycle[0] = True
        return []

    temporary_visited[index] = True

    for i in graph[index]:
        toposort(graph, i, temporary_visited, permanent_visited, result, cycle)

    temporary_visited[index] = False
    permanent_visited[index] = True
    result.append(index)
    return result

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
        temporary_visited = [False for i in range(numCourses)]
        permanent_visited = [False for i in range(numCourses)]
        cycle = [False]
        result = []
        for i in range(numCourses):
            if not permanent_visited[i]:
                toposort(graph, i, temporary_visited, permanent_visited, result, cycle)
        if not cycle[0]:
            return result
        else:
            return []