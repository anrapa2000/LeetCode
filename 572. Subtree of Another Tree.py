# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        def isIdentical(p, q):
            if p is None and q is None:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isIdentical(p.left, q.left) or isIdentical(p.right, q.right)

        if root is None:
            return False
        if isIdentical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(2)
subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)
print(Solution().isSubtree(root, subRoot))
