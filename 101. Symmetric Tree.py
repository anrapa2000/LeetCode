# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def symmetric(node1, node2):
            if root is None:
                return True
            if node1 is None and node2 is None:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return symmetric(node1.left, node2.right) and symmetric(
                node2.left, node1.right
            )

        if not root:
            return True
        return symmetric(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
value = Solution()
print(value.isSymmetric(root))
