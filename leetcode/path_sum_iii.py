class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def parsesum(root, sum):
            if not root:
                return 0
            if root.val == sum:
                return 1 + parsesum(root.left, sum - root.val) + parsesum(root.right, sum - root.val)
            return parsesum(root.left, sum - root.val) + parsesum(root.right, sum - root.val)

        if not root:
            return 0

        return parsesum(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)