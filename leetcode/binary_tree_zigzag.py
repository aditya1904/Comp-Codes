# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def levelwise(root: TreeNode, n, res):
    global max_level
    if ( n == -1):
        max_level = -1
    if (n > max_level):
        max_level = n
        res.append([])
    if(root):
        level = n + 1
        levelwise(root.right, level, res)
        levelwise(root.left, level, res)
        if level%2 != 0:
            res[level].append(root.val)
        else:
            res[level] = [root.val] + res[level]
        return res
    else:
        return []

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = levelwise(root, -1, [])
        return res