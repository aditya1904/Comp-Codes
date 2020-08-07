# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.vert  = []
        self.dictionary = defaultdict(lambda : [])
        def levelwise(root, x_coord, y_coord):
            if root:
                self.vert.append((x_coord, y_coord, root.val))
                levelwise(root.left, x_coord - 1, y_coord - 1)
                levelwise(root.right, x_coord + 1, y_coord - 1)

        levelwise(root, 0, 0)
        sorted_vert = sorted(self.vert, key=lambda tup :(tup[0], -tup[1], tup[2]))
        for tup in sorted_vert:
            self.dictionary[tup[0]].append(tup[2])
        return self.dictionary.values()