class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = []
        result = []
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                value = queue.pop(0)
                if value.left: queue.append(value.left)
                if value.right: queue.append(value.right)
                temp.append(value.val)
            result.append(temp)
        return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))