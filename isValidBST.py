# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validBSTRange(node, range):
            if node and node.left:
                if node.val <= node.left.val and node.left.val > range:
                    return False
            if node and node.right: 
                 if node.val >= node.right.val and node.right.val < range:
                     return False
            return True
    
        if root is None:
            return True
        rootValue = root.val
        return validBSTRange(root, rootValue) 
        # rootValue = root.val
        # if root and root.left: 
        #     if root.val <= root.left.val:
        #         return False
        # if root and root.right: 
        #     if root.val >= root.right.val:
        #         return False
        # return self.validBSTRange(root.left) and self.isValidBST(root.right)
