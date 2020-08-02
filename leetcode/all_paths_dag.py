def getpath(graph, node, path, finalnode, paths):
    path.append(node)
    if node == finalnode:
        paths.append(path)
        return path
    for edge in graph[node]:
        temppath = path[:]
        getpath(graph, edge, path, finalnode, paths)
        path = temppath[:]

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        path = []
        finalnode = len(graph) - 1
        getpath(graph, 0, path, finalnode, paths)
        return paths